import cv2
from PIL import Image
import numpy as np
import math
import imageio as iio
from imutils import resize, rotate
from collections import defaultdict
from datetime import datetime



def corrigir_perspectiva(imagem):
    global tentativas, spec
    # Aplicar a detecção de bordas com o algoritmo Canny e threshold entre 170 e 255
    bordas = cv2.Canny(imagem, 170, 255)

    # Aplicar operações de dilatação e erosão para melhorar os contornos dos retângulos
    kernel = np.ones((5, 5), np.uint8)
    bordas = cv2.dilate(bordas, kernel, iterations=1)
    bordas = cv2.erode(bordas, kernel, iterations=1)

    # Encontrar os contornos na imagem de bordas
    contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar o retângulo de maior área no meio da imagem
    maior_area = 0
    retangulo = None
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > maior_area and area < (imagem.shape[0] * imagem.shape[1] * 0.9):  # Descartar contornos muito grandes
            perimetro = cv2.arcLength(contorno, True)
            aprox_poligono = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
            if len(aprox_poligono) == 4:  # Verificar se é um retângulo
                maior_area = area
                retangulo = aprox_poligono

    # Definir os pontos de referência na imagem original e na imagem de destino
    pontos_origem = np.float32(retangulo.reshape(4, 2))
    pontos_destino = np.float32([[0, 0], [imagem.shape[1], 0], [imagem.shape[1], imagem.shape[0]], [0, imagem.shape[0]]])

    # Calcular a matriz de transformação perspectiva
    matriz_transformacao = cv2.getPerspectiveTransform(pontos_origem, pontos_destino)

    # Aplicar a transformação perspectiva na imagem
    imagem_corrigida = cv2.warpPerspective(imagem, matriz_transformacao, (imagem.shape[1], imagem.shape[0]))
    imagem_corrigida = cv2.flip(cv2.rotate(cv2.resize(imagem_corrigida, (imagem_corrigida.shape[0], imagem_corrigida.shape[1])), cv2.ROTATE_90_CLOCKWISE), 1)

    detection_image = imagem_corrigida
    lscale_percent = 25  # percent of original size
    width = int(detection_image.shape[1] * lscale_percent / 100)
    height = int(detection_image.shape[0] * lscale_percent / 100)
    #cv2.imwrite(f"tentativas/{spec} - {str(tentativas)} r.jpg", detection_image)
    #cv2.imshow("teste", resize(detection_image, width, height))
    #cv2.waitKey(20)

    return imagem_corrigida

def melhorResultado(resultados):
    melhorResultado = []
    alternativas_marcadas = defaultdict(lambda: defaultdict(int))

    # Contagem das alternativas marcadas em cada questão
    for resultado in resultados:
        for questao, alternativa in resultado:
            alternativas_marcadas[questao][alternativa] += 1

    # Identificação das alternativas mais marcadas em cada questão
    for questao, alternativas in alternativas_marcadas.items():
        max_ocorrencias = max(alternativas.values())
        melhorResultado.append((questao, [alt for alt, ocorrencias in alternativas.items() if ocorrencias == max_ocorrencias][0]))
    return melhorResultado
    

def organizar(resultados):
    dadospquestao = {}
    for r in resultados:
        dadospquestao.setdefault(r[0], []).append(r[1])

    certos = []
    for q, respostas in dadospquestao.items():
        c = max('ABCDE', key=respostas.count)
        if len(respostas) <= 6:
            certos.append((q, c))
        else:
            certos.append((q, "INVÁLIDO"))
    certos.sort(key=lambda a: a[0])

    return certos


def getCamera():
    global camera
    if 'camera' not in globals() or camera == None:
        camera = iio.get_reader("<video1>")
getCamera()

def getVideoFeed():
    global camera
    getCamera()
    screenshot = camera.get_next_data()
    screenshot = Image.fromarray(screenshot)
    screenshot = np.array(screenshot)

    vid = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    frame = vid
    return frame

tentativas = 1
spec = 0

def scan(webcamframe, RESIZEFACTOR, s=-1):
    global tentativas, spec, resultados
    resultados = [] 
    cascade = cv2.CascadeClassifier('classifierGeral/cascade.xml')
    cascade2 = cv2.CascadeClassifier('classifierMarcadas/cascade.xml')
    fixed = False
    tol = 200
    if s != -1:
        spec = s
    scale_percent = RESIZEFACTOR
    
    rts = [0, 5, -5, 3, -3]
    rectangles = []
    rectangles2 = []
    webcamframe = cv2.rotate(webcamframe, cv2.ROTATE_90_CLOCKWISE)

    while True:
        
        gray = cv2.cvtColor(webcamframe, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 170, 255,
		cv2.THRESH_BINARY_INV)[1]
        frame = rotate(thresh, rts[tentativas%5])
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_LINEAR)
        imrgb = cv2.resize(rotate(webcamframe, rts[tentativas%5]), dim, interpolation=cv2.INTER_LINEAR)
        questão = 1
        item = 0
        itens = "ABCDE"
        index = 0

        linhas = []
        linha = 0

        results = []
        
        
        if not fixed:
            rectangles = list(cascade.detectMultiScale(frame))
            rectangles2 = list(cascade2.detectMultiScale(frame))
            rectangles += rectangles2
        
        if len(rectangles)>0:
            default = (int((rectangles[0][2] + rectangles[-1][2]) / 2), int((rectangles[0][3] + rectangles[-1][3]) / 2))
            for r in range(len(rectangles)):
                x, y, w, h = rectangles[r]
                dif = (w - default[0], h - default[1])

                if np.isin(rectangles[r], rectangles2).all():
                    w = np.where(rectangles2 == rectangles[r])
                    try:
                        index = w[0][0]
                        rectangles2[index] = x + int(dif[0] / 2), y + int(dif[1] / 2), rectangles[0][2], rectangles[0][3]
                    except:
                        pass
                rectangles[r] = x + int(dif[0] / 2), y + int(dif[1] / 2), rectangles[0][2], rectangles[0][3]

            rectangles.sort(key=lambda rect: (math.ceil(rect[1] / 100) * 100 / 50 * scale_percent,
                                            math.ceil(rect[0] / 100) * 100 / 50 * scale_percent))

            index = 0
            for r in rectangles:
                x, y, w, h = r
                if index == 0:
                    linhas.append([r])

                if abs(linhas[linha][-1][0] - x) <= tol:
                    if abs(linhas[linha][-1][0] - x) >= tol / 3:
                        linhas[linha].append(r)
                else:
                    linhas.append([r])
                    linha += 1

                if len(linhas[linha]) > len(itens):
                    linhas[linha].pop(0)

                index += 1

            questoesValidas = []
            for c in linhas:
                if len(c) == 5:
                    questoesValidas.append(c)
                    """
                    cor = (0, 0, 255) if np.isin(c, rectangles2).all() else (255, 255, 0)
                else:
                    cor = (255, 0, 255)
                cv2.rectangle(imrgb, (c[0][0], c[0][1]), (c[-1][0] + c[-1][2], c[-1][1] + c[-1][3]), cor, 2)"""
            questoesValidas.sort(key=lambda a: (a[0][1], a[0][0]))


            for l in questoesValidas:
                try:
                    l.sort(key=lambda a: l[0])
                except:
                    pass
                for item, r in enumerate(l):
                    x, y, w, h = r
                    if item == 0:
                        q = questão
                        if q % 2 == 0:
                            q = int(questão / 2 + 10)
                        else:
                            q = int((questão + 1) / 2)
                    if np.isin(r, rectangles2).all():
                        results.append((q, itens[item % len(itens)]))

                    """    cor = (255, 0, 255)
                    else:
                        cor = (255, 255, 255)
                    cv2.putText(imrgb, str(itens[item % 5]), (int(r[0]) + int(r[2] / 3), int(r[1]) + int(r[3] / 1.5)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2, cv2.LINE_AA)
                    cv2.rectangle(imrgb, (x, y), (x + w, y + h), (0, 255, 0), 1)"""

                    item += 1
                questão += 1
        detection_image = rotate(imrgb, -rts[tentativas%5])

        lscale_percent = 25  # percent of original size
        width = int(detection_image.shape[1] * lscale_percent / 100)
        height = int(detection_image.shape[0] * lscale_percent / 100)
        #cv2.imshow("teste", resize(detection_image, width, height))
        st = datetime.now().strftime('%d-%m-%Y%H-%M-%S')
        #cv2.imwrite(f"tentativas/{st}.jpg", detection_image)
        #cv2.waitKey(20)
        dim = (width, height)

        if len(results) > 0:
            resultados.append(results)
            melhorResultado(resultados)

        tentativas += 1
        
        if tentativas >= 10:
            return len(resultados) > 5, organizar(melhorResultado(resultados))
        
        if len(resultados) > 4:
            melhorResultado(resultados)
            return True, organizar(melhorResultado(resultados))
