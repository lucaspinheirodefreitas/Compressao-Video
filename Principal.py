# # -*- coding: utf-8 -*-

from CompressaoFFMPEG import CompressaoFFMPEG
# from Estatisticas import

class Principal(object):
        video_ffmpeg = CompressaoFFMPEG()
        video_ffmpeg.compressaoMPEG()
        print(video_ffmpeg.tempo)
        print(video_ffmpeg.tamanho_inicial)
        print(video_ffmpeg.tamanho_final)
