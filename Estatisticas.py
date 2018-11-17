# -*- coding: utf-8 -*-

import matplotlib

class Estatisticas(object):
    def __init__(self, tempo, tamanho_inicial, tamanho_final):
        self.tempo = tempo
        self.tamanho_inicial = tamanho_inicial
        self.tamanho_final = tamanho_final

    def imprime_dados(self):
        print("\nO tempo gasto para comprimir o video foi: %d " % self.tempo + ("segundos." if (self.tempo > 1) else "segundo."))
        print("O tamanho inicial do video era: %.3f MBs." % (self.tamanho_inicial/1000000.0))
        print("O tamanho final do video é: %.3f MBs." % (self.tamanho_final/1000000.0))
