# -*- coding: utf-8 -*-

import matplotlib

class Estatisticas(object):
    def __init__(self, tempo, tamanho_inicial, tamanho_final):
        self.tempo = tempo
        self.tamanho_inicial = tamanho_inicial
        self.tamanho_final = tamanho_final

    def coleta_dados(self):
        print("O tempo gasto para comprimir o video foi: %d segundos." % self.tempo)
        print("O tamanho inicial do video era: %d bytes." % self.tamanho_inicial)
        print("O tamanho final do video é: %d bytes." % self.tamanho_final)
