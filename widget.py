# This Python file uses the following encoding: utf-8
#import os
from concurrent.futures import thread
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, QPushButton, QGraphicsDropShadowEffect, QDialog, QStackedWidget, QFileDialog, QVBoxLayout, QTabWidget, QHBoxLayout, QLabel, QDoubleSpinBox, QComboBox, QListWidget
from PySide6.QtCore import QFile, QPointF, Qt, QThread, Signal, Slot, QRect, QCoreApplication
from PySide6.QtGui import QImage, QPixmap, QColor, QPainter, QBrush, QPainterPath, QRegion, QCursor
from PySide6.QtUiTools import QUiLoader
import pickle
import cv2
frame = []

class Thread(QThread):
    changePixmap = Signal(QImage)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.a = 1

    def run(self):
        import MLM
        global webcamLabel, frame
        global webcamFrame

        done = False
        while True:
            self.a += 1
            if not done:
                self.scanbutton.setEnabled(True)
                self.scanbutton.setText("Escanear")
                done = True
            vid = MLM.getVideoFeed()
            frame = vid
            rgbImage = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            p = convertToQtFormat.scaled(480, 360, Qt.KeepAspectRatio)

            webcamFrame = rgbImage

            webcamLabel.setFixedWidth(p.width())
            webcamLabel.setFixedHeight(p.height())

            self.changePixmap.emit(p)


class Gabarito(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        import MLM
        global caminho
        self.load_ui()

        self.gabaritoWidget = self.findChild(QListWidget, "listWidget")
        self.arquivoWidget = self.findChild(QLineEdit, "lineEdit_4")
        self.arquivoWidget.setText(caminho)
        self.serieWidget = self.findChild(QLineEdit, "lineEdit_6")
        self.turmaWidget = self.findChild(QLineEdit, "lineEdit_7")
        self.questoesWidget = self.findChild(QLineEdit, "lineEdit_5")

        self.gabaritoAtualWidget = self.findChild(QLabel, "label_2")
        self.proximoButton = self.findChild(QPushButton, "pushButton_3")
        self.proximoButton.clicked.connect(self.proximo)
        self.anteriorButton = self.findChild(QPushButton, "pushButton_4")
        self.anteriorButton.clicked.connect(self.anterior)

        self.acertosWidget = self.findChild(QLabel, "acertoslabel")
        self.notaWidget = self.findChild(QLabel, "notalabel")
        self.cores = ["color:rgb(50, 170, 50)", "color:rgb(170, 50, 50)"]

        self.filebutton = self.findChild(QPushButton, "pushButton_5")
        self.filebutton.clicked.connect(self.openFileNameDialog)

        self.returnbutton = self.findChild(QPushButton, "pushButton_6")
        self.returnbutton.clicked.connect(self.voltar)

        self.gabaritoAtual = 1

        with open(self.arquivoWidget.text(), 'rb') as handle:
            self.info = pickle.load(handle)

        self.atualizar()

    def proximo(self):
        if self.gabaritoAtual < self.info['alunos']:
            self.gabaritoAtual += 1
        self.atualizar()

    def anterior(self):
        if self.gabaritoAtual > 1:
            self.gabaritoAtual -= 1
        self.atualizar()

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "gabarito.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        self.showMaximized()


    def voltar(self):
        import MLM
        try:
            MLM.stop()
        except:
            pass
        widget.addWidget(TelaPrincipal())
        widget.removeWidget(self)

        self.close()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.ShowDirsOnly
        fileName = QFileDialog.getOpenFileName(options = options)
        if fileName:
            self.arquivoWidget.setText(fileName[0])
        
        with open(fileName[0], 'rb') as handle:
            self.info = pickle.load(handle)
        self.notaWidget.setText('')
        self.acertosWidget.setText('')
        self.gabaritoAtual = 1
        self.atualizar()
            
    def atualizar(self):
        self.serieWidget.setText(self.info['série'])
        self.turmaWidget.setText(self.info['curso'])
        self.questoesWidget.setText(str(self.info['questões']))
        self.gabaritoAtualWidget.setText(f"{self.gabaritoAtual}/{self.info['alunos']}")

        self.gabaritoWidget.clear()

        try:
            acertos = 0
            for questão in self.info['dados'][self.gabaritoAtual-1]:
                alternativa = self.info["dados"][self.gabaritoAtual-1][questão]
                if len(questão) <= 9:
                    if alternativa != "INVÁLIDO":
                        s = questão + f'    ({alternativa})'
                    else:
                        s = questão + f'    INVÁLIDA'
                else:
                    s = questão + f'  ({self.info["dados"][self.gabaritoAtual-1][questão]})'
                if alternativa == self.info['matriz'][questão]:
                    s += " ✓"
                    acertos += 1
                else:
                    s += " ✗"
                
                self.gabaritoWidget.addItem(s)
            
            nota = acertos/self.info['questões']*10

            if nota >= 6:
                self.notaWidget.setStyleSheet(self.cores[0])
            else:
                self.notaWidget.setStyleSheet(self.cores[1])
            
            self.notaWidget.setText(str(round(nota, 1)).replace(".", ","))
            self.acertosWidget.setText(f"Nota:")
        except:
            self.notaWidget.setText('')
            self.acertosWidget.setText('')
            self.gabaritoWidget.addItem("[Vazio]")

class TelaPrincipal(QDialog):
    def __init__(self, parent=None):
        global scanbutton
        super().__init__(parent)
        self.load_ui()
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.openFileNameDialog)

        self.gabaritoAtual = 0

        self.scanbutton = self.findChild(QPushButton, "pushButton_2")
        self.scanbutton.clicked.connect(self.escanear)
        self.nextbutton = self.findChild(QPushButton, "pushButton_3")
        self.nextbutton.clicked.connect(self.proximo)

        self.previousbutton = self.findChild(QPushButton, "pushButton_4")
        self.previousbutton.clicked.connect(self.anterior)

        self.searchbutton = self.findChild(QPushButton, "pushButton_5")
        self.searchbutton.clicked.connect(self.gabaritoFuncao)

        self.gabaritoWidget = self.findChild(QLabel, "label_12")
        self.serieWidget = self.findChild(QComboBox, "comboBox")
        self.cursoWidget = self.findChild(QComboBox, "comboBox_2")
        self.alunosWidget = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.questoesWidget = self.findChild(QDoubleSpinBox, "doubleSpinBox_2")
        self.avaliacaoWidget = self.findChild(QLineEdit, "lineEdit_2")
        self.pastaWidget = self.findChild(QLineEdit, "lineEdit")

        self.serieWidget.currentIndexChanged.connect(self.atualizar)
        self.cursoWidget.currentIndexChanged.connect(self.atualizar)
        self.alunosWidget.valueChanged.connect(self.atualizar)
        self.questoesWidget.valueChanged.connect(self.atualizar)
        self.pastaWidget.textChanged.connect(self.atualizar)

        self.informações = {}
        self.dados = []
        self.matriz = []

        self.atualizar()

    def gabaritoFuncao(self):
        import MLM

        self.th.terminate()
            
        while MLM.camera:
            MLM.camera = None

        widget.addWidget(Gabarito())

        widget.removeWidget(self)

        self.close()

    def escanear(self):
        import MLM
        global webcamFrame
        global frame
        self.scanbutton.setCursor(Qt.WaitCursor)
        self.th.terminate()
        s = MLM.scan(frame, True, 325)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.scanbutton = scanbutton
        self.th.start()

        self.scanbutton.setCursor(Qt.PointingHandCursor)
        if s[0]: #Se der certo
            if self.gabaritoAtual < self.alunos:
                self.gabaritoAtual += 1

            fin = {}
            for q in s[1]:
                fin[f"Questão {q[0]}"] = q[1]
            self.dados.append(fin)

        self.atualizar()

    def atualizar(self):
        global caminho
        self.serie = self.serieWidget.currentText()
        self.curso = self.cursoWidget.currentText()
        self.questoes = int(self.questoesWidget.value())
        self.alunos = int(self.alunosWidget.value())
        self.pasta = self.pastaWidget.text()
        self.avaliacao = self.avaliacaoWidget.text()
        if self.gabaritoAtual > 0:
            self.gabaritoWidget.setText(f"Gabarito {self.gabaritoAtual}/{self.alunos}")
        else:
            self.gabaritoWidget.setText(f"Gabarito {self.gabaritoAtual}/{self.alunos} (Matriz)")
        if len(self.dados) > 0:
            self.matriz = self.dados[0]


        self.informações = {'série':self.serie,
                            'curso':self.curso,
                            'questões':self.questoes,
                            'alunos':self.alunos,
                            'avaliacao':self.avaliacao,
                            'dados':self.dados[1::],
                            'matriz':self.matriz}
        
        caminho = self.pasta + f'/{self.avaliacao}.dat'

        with open(caminho, 'wb') as handle:
            pickle.dump(self.informações, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def proximo(self):
        if self.gabaritoAtual < self.alunos:
            self.gabaritoAtual += 1
        self.atualizar()

    def anterior(self):
        if self.gabaritoAtual > 0:
            self.gabaritoAtual -= 1
        self.atualizar()

    @Slot(QImage)
    def setImage(self, image):
        imgsize = min(image.width(), image.height())
        out_img = QImage(image.width(), image.height(), QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)


        # Create a texture brush and paint a circle with the original image onto
        # the output image:
        brush = QBrush(image)        # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)      # Use the image texture brush
        painter.setPen(Qt.NoPen)     # Don't draw an outline
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawRoundedRect(0, 0, image.width(), image.height(), 20, 20)  # Actually draw the circle
        painter.end()                # We are done (segfault if you forget this)

        self.label.setPixmap(QPixmap.fromImage(out_img))

    def load_ui(self):
        global webcamLabel
        global scanbutton
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "mainwindow.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        self.showMaximized()

        self.label = self.findChild(QLabel, name="label_9")
        webcamLabel = self.label

        scanbutton = self.findChild(QPushButton, "pushButton_2")

        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.scanbutton = scanbutton
        self.th.start()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        fileName = QFileDialog.getExistingDirectory(options = options)
        if fileName:
            self.pastaWidget.setText(fileName)
        self.atualizar()


class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

        self.gridFrame = self.findChild(QFrame, "gridFrame")
        self.nomeInput = self.findChild(QLineEdit, "usuarioInput")
        self.senhaInput = self.findChild(QLineEdit, "senhaInput")
        self.button = self.findChild(QPushButton)
        self.button.clicked.connect(self.loginFuncao)

        #shadow = QGraphicsDropShadowEffect(blurRadius=9.0, offset=QPointF(8.0, 8.0))
        #self.gridFrame.setGraphicsEffect(shadow)

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "login.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        self.showMaximized()

    def loginFuncao(self):
        usuário = self.nomeInput.text()
        senha = self.senhaInput.text()
        if usuário == 'Professor' and senha == '1234':
            widget.addWidget(TelaPrincipal())
            widget.removeWidget(self)

            self.close()


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    widget.addWidget(Login())

    
    widget.setFixedWidth(1366)
    widget.setFixedHeight(768)
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.showMaximized()
    app.setStyle('Oxygen')
    sys.exit(app.exec())
