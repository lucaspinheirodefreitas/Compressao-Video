# # -*- coding: utf-8 -*-

class PathVideos(object):

    def __init__(self):
        #self.VIDEO_ENTRADAC1 = 'H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4'
        #self.VIDEO_ENTRADAC2 = 'MPEG-2 vs H.264.mp4'
        #self.VIDEO_ENTRADAC3 = 'The Personal Computer Revolution- Crash Course Computer Science #25.mp4'
        #self.VIDEO_ENTRADAC4 = 'video.mp4'
        self.VIDEO_ENTRADAC4 = 'video.mp4'
        #self.VIDEO_SAIDAC1 = 'convert-H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4'
        #self.VIDEO_SAIDAC2 = 'convert-MPEG-2 vs H.264.mp4'
        #self.VIDEO_SAIDAC3 = 'convert-The Personal Computer Revolution- Crash Course Computer Science #25.mp4'
        self.VIDEO_SAIDAC4 = 'convert-video.mp4'
        self.LOCAL_VIDEOS = '/home/mohammed/Área de trabalho/UFABC/2018/Q3 - 2018/AED-II/Projeto/Videos/'
        self.VIDEOS_ENTRADA = [#self.LOCAL_VIDEOS + VIDEO_ENTRADAC1,
                                         #self.LOCAL_VIDEOS + VIDEO_ENTRADAC2,
                                         #self.LOCAL_VIDEOS + VIDEO_ENTRADAC3,
                                         self.LOCAL_VIDEOS + self.VIDEO_ENTRADAC4]
        self.VIDEOS_SAIDA = [#self.LOCAL_VIDEOS + VIDEO_SAIDAC1,
                                       #self.LOCAL_VIDEOS + 'Videos-convertidos/' + VIDEO_SAIDAC2,
                                       #self.LOCAL_VIDEOS + VIDEO_SAIDAC3,
                                       self.LOCAL_VIDEOS + 'Videos-convertidos/' + self.VIDEO_SAIDAC4]
'''
    for i, num in enumerate(VIDEOS_ENTRADA):
        print(VIDEOS_ENTRADA[i])
'''
