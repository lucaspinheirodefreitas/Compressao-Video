# # -*- coding: utf-8 -*-

from CompressaoFFMPEG import CompressaoFFMPEG
from Estatisticas import Estatisticas

class Principal(object):
        video_ffmpeg = CompressaoFFMPEG()
        video_ffmpeg.compressaoMPEG()
        video_ffmpeg.compressaoH264()
        informacoes = Estatisticas(video_ffmpeg.tamanho_inicial_mpeg4, video_ffmpeg.videos.numero_videos)
        informacoes.plota_comparativo(video_ffmpeg.tamanho_final_h264, video_ffmpeg.tempo_h264, video_ffmpeg.tamanho_final_mpeg4, video_ffmpeg.tempo_mpeg4)
