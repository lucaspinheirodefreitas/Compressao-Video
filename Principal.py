# # -*- coding: utf-8 -*-

from CompressaoFFMPEG import CompressaoFFMPEG
from Estatisticas import Estatisticas

class Principal(object):
        video_ffmpeg = CompressaoFFMPEG()
        video_ffmpeg.compressaoMPEG()
        informacoes = Estatisticas(video_ffmpeg.tempo, video_ffmpeg.tamanho_inicial, video_ffmpeg.tamanho_final)
        informacoes.coleta_dados()
