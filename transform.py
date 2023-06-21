import cv2
import numpy as np
from imutils import resize, rotate

def corrigir_perspectiva(imagem):
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
    

    return imagem_corrigida


# Exemplo de uso
# Carregar a imagem original

im = cv2.imread('C:/Users/Marco/Desktop/Corretor pro Edvar/Completa.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imagem_original = gray
#imagem_original = cv2.imread('255.jpg')#cv2.imread('C:/Users/Marco/Desktop/Corretor pro Edvar/Completa.jpg', cv2.IMREAD_GRAYSCALE)
thresh = cv2.threshold(imagem_original, 170, 255,
		cv2.THRESH_BINARY_INV)[1]
imagem_original = thresh
cv2.imwrite("Oxe.jpg", thresh)


# Aplicar a correção de perspectiva
imagem_corrigida = corrigir_perspectiva(rotate(thresh, -5))

# Exibir a imagem original e a imagem corrigida
cv2.imshow('Imagem Original', cv2.resize(imagem_original, (int(imagem_original.shape[1]/7), int(imagem_original.shape[0]/7))))
cv2.imshow('Imagem Corrigida', cv2.resize(imagem_corrigida, (int(imagem_corrigida.shape[1]/7), int(imagem_corrigida.shape[0]/7))))
cv2.waitKey(0)
cv2.destroyAllWindows()