import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if(ret is True):
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        break
    cv2.imshow('frame',color)
    # cv2.imshow('frame',ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
    Possibilidades de transformação de um video em MPEG, utilizando o comando OS
    de python e escrevendo o comando necessário para rodar o FFMPEG via terminal
    ou utilizar a biblioteca ffpy ou ffmpeg-python

    A seguir tem dois métodos possiveis de utilização do FFMPEG, tanto através da biblioteca OS, quanto, subprocess.

    import subprocess
    subprocess.call('ffmpeg -i video.mp4 -vcodec libx264 -crf 20 parte4-convertido.mp4', shell=True)

    import os
    os.system("ffmpeg -i video.mp4 -vcodec libx264 -crf 20 parte4-convertido.mp4")

    versão e breve descritivo do utilitario utilizado
    ffmpeg version 3.2.12-1~deb9u1 Copyright (c) 2000-2018 the FFmpeg developers


'''
