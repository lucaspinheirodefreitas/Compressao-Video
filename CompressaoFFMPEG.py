# # -*- coding: utf-8 -*-

import timeit
import os
from PathVideos import PathVideos

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

class CompressaoFFMPEG(object):

    def __init__(self):
        self.videos = (PathVideos())
        self.tempo_mpeg4 = 0
        self.tamanho_inicial_mpeg4 = 0
        self.tamanho_final_mpeg4 = 0
        self.tempo_h264 = 0
        self.tamanho_inicial_h264 = 0
        self.tamanho_final_h264 = 0

    def compressaoMPEG(self):
        self.videos.new_path()
        for i, local in enumerate(self.videos.VIDEOS_ENTRADA):
            self.tamanho_inicial_mpeg4 = self.tamanho_video(self.videos.VIDEOS_ENTRADA[i])
            tempo_i = self.calc_timer()
            os.system('ffmpeg -i ' + ('\"' + self.videos.VIDEOS_ENTRADA[i] + '\"') + ' -vcodec libxvid -crf 20 '
            + ('\"' + self.videos.VIDEOS_SAIDA[i] + "-mpeg4.mp4" + '\"'))
            tempo_f = self.calc_timer()
            self.tamanho_final_mpeg4 = self.tamanho_video(self.videos.VIDEOS_SAIDA[i] + "-mpeg4.mp4")
            self.tempo_mpeg4 = (tempo_f - tempo_i)

    def compressaoH264(self):
        for i, local in enumerate(self.videos.VIDEOS_ENTRADA):
            self.tamanho_inicial_h264 = self.tamanho_video(self.videos.VIDEOS_ENTRADA[i])
            tempo_i = self.calc_timer()
            os.system('ffmpeg -i ' + ('\"' + self.videos.VIDEOS_ENTRADA[i] + '\"') + ' -vcodec libx264 -crf 20 '
            + ('\"' + self.videos.VIDEOS_SAIDA[i] + "-h264.mp4" + '\"'))
            tempo_f = self.calc_timer()
            self.tamanho_final_h264 = self.tamanho_video(self.videos.VIDEOS_SAIDA[i] + "-h264.mp4")
            self.tempo_h264 = (tempo_f - tempo_i)

    def calc_timer(self):
        tempo = timeit.default_timer()
        return tempo

    def tamanho_video(self, VIDEO):
        tamanho = os.path.getsize(VIDEO)
        return tamanho
