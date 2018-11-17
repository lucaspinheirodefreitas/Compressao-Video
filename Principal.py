# # -*- coding: utf-8 -*-

from CompressaoFFMPEG import CompressaoFFMPEG
from Estatisticas import Estatisticas

class Principal(object):
        video_ffmpeg = CompressaoFFMPEG()
        video_ffmpeg.compressaoMPEG()
        video_ffmpeg.compressaoH264()
        informacoesMPEG = Estatisticas(video_ffmpeg.tempo_mpeg4, video_ffmpeg.tamanho_inicial_mpeg4, video_ffmpeg.tamanho_final_mpeg4)
        informacoesMPEG.imprime_dados()
        informacoesH264 = Estatisticas(video_ffmpeg.tempo_h264, video_ffmpeg.tamanho_inicial_h264, video_ffmpeg.tamanho_final_h264)
        informacoesH264.imprime_dados()
