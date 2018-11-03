# # -*- coding: utf-8 -*-

from CompressaoFFMPEG import CompressaoFFMPEG
# from Estatisticas import

class Principal(object):
        video_ffmpeg = CompressaoFFMPEG()
        video_ffmpeg.compressaoMPEG()
        Estatisticas(video_ffmpeg.tempo, video_ffmpeg.tamanho_inicial, video_ffmpeg.tamanho_final)
