import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Carregue o rastreador


# Leia o primeiro quadro do vídeo


# Selecione a caixa delimitadora na imagem


# Inicialize o rastreador em img e na caixa delimitadora


def drawBox(img, bbox):
    

while True:
    
    check, img = video.read()   

    # Atualize o rastreador em img e na caixa delimitadora
    

   

    cv2.imshow("resultado", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()
