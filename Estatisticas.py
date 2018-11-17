# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

class Estatisticas(object):
    def __init__(self, tamanho_inicial, numero_videos):
        self.tamanho_inicial = tamanho_inicial
        self.numero_videos = numero_videos
        self.tamanho_final_h264 = []
        self.tempo_h264 = []
        self.tamanho_final_mpeg4 = []
        self.tempo_mpeg4 = []
        self.nm_videos = []
    '''
    def imprime_dados(self):
        for i in range(self.numero_videos):
            print("\nO tempo gasto para comprimir o video foi: %d " % self.tempo[i] + ("segundos." if (self.tempo[i] > 1) else "segundo."))
            print("O tamanho inicial do video era: %.3f MBs." % (self.tamanho_inicial[i]/1000000.0))
            print("O tamanho final do video é: %.3f MBs." % (self.tamanho_final[i]/1000000.0))
    '''

    '''
    Como utilizar a biblioteca matplotlib:
        https://www.vooo.pro/insights/guia-basico-para-plotar-graficos-usando-o-matplotlib-do-python/
        https://www.vooo.pro/insights/guia-basico-para-plotar-graficos-usando-o-matplotlib-do-python-parte-2/
    '''

    def nome_videos(self):
        for i in range(self.numero_videos):
            self.nm_videos.append("video" + str(i+1))
        return self.nm_videos

    def plota_comparativo(self, tamanho_final_h264, tempo_h264, tamanho_final_mpeg4, tempo_mpeg4):
        fig, ax = plt.subplots()
        indice = np.arange(self.numero_videos)
        bar_larg = 0.4
        transp = 0.8
        plt.bar(indice, tamanho_final_mpeg4, bar_larg, alpha=transp, color="orange", label='compressaoMPEG')
        plt.bar(indice + bar_larg, tamanho_final_h264, bar_larg, alpha=transp, color="gray", label='compressaoH264')

        plt.xlabel('quantidade de videos')
        plt.ylabel('tamanho do video')
        plt.title('Compressao H264 x MPEG')
        plt.xticks(indice + (bar_larg/2), self.nome_videos())
        plt.legend()
        plt.tight_layout()
        plt.show()
