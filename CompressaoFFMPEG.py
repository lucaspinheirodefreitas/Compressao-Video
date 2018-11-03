# # -*- coding: utf-8 -*-

import timeit
import os
from PathVideos import PathVideos

class CompressaoFFMPEG(object):

    def __init__(self):
        self.videos = (PathVideos())
        self.tempo = 0
        self.tamanho_inicial = 0
        self.tamanho_final = 0

    def compressaoMPEG(self):
        for i, local in enumerate(self.videos.VIDEOS_ENTRADA_COM_ASPAS):
            self.tamanho_inicial = self.tamanho_video(self.videos.VIDEOS_ENTRADA_SEM_ASPAS[i])
            tempo_i = self.calc_timer()
            os.system('ffmpeg -i ' + self.videos.VIDEOS_ENTRADA_COM_ASPAS[i] + ' -vcodec libx264 -crf 20 '
            + self.videos.VIDEOS_SAIDA_COM_ASPAS[i])
            tempo_f = self.calc_timer()
            self.tamanho_final = self.tamanho_video(self.videos.VIDEOS_SAIDA_SEM_ASPAS[i])
            self.tempo = (tempo_f - tempo_i)


    def calc_timer(self):
        tempo = timeit.default_timer()
        return tempo

    def tamanho_video(self, VIDEO):
        print(VIDEO)
        tamanho = os.path.getsize(VIDEO)
        return tamanho
