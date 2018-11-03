# # -*- coding: utf-8 -*-

class PathVideos(object):

    def __init__(self):
        #self.VIDEO_ENTRADAC1 = 'H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4\''
        #self.VIDEO_ENTRADAC2 = 'MPEG-2 vs H.264.mp4\''
        #self.VIDEO_ENTRADAC3 = 'The Personal Computer Revolution- Crash Course Computer Science #25.mp4\''
        self.VIDEO_ENTRADAC4 = 'video.mp4\"'
        #self.VIDEO_SAIDAC1 = 'convert-H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4\''
        #self.VIDEO_SAIDAC2 = 'convert-MPEG-2 vs H.264.mp4\''
        #self.VIDEO_SAIDAC3 = 'convert-The Personal Computer Revolution- Crash Course Computer Science #25.mp4\''
        self.VIDEO_SAIDAC4 = 'convert-video.mp4\"'
        self.LOCAL_VIDEOS_COM_ASPAS = '\"/home/mohammed/Área de trabalho/UFABC/2018/Q3 - 2018/AED-II/Projeto/Videos/'
        self.VIDEOS_ENTRADA_COM_ASPAS = [#self.LOCAL_VIDEOS_COM_ASPAS + VIDEO_ENTRADAC1,
                                         #self.LOCAL_VIDEOS_COM_ASPAS + VIDEO_ENTRADAC2,
                                         #self.LOCAL_VIDEOS_COM_ASPAS + VIDEO_ENTRADAC3,
                                         self.LOCAL_VIDEOS_COM_ASPAS + self.VIDEO_ENTRADAC4]
        self.VIDEOS_SAIDA_COM_ASPAS = [#self.LOCAL_VIDEOS_COM_ASPAS + VIDEO_SAIDAC1,
                                       #self.LOCAL_VIDEOS_COM_ASPAS + 'Videos-convertidos/' + VIDEO_SAIDAC2,
                                       #self.LOCAL_VIDEOS_COM_ASPAS + VIDEO_SAIDAC3,
                                       self.LOCAL_VIDEOS_COM_ASPAS + 'Videos-convertidos/' + self.VIDEO_SAIDAC4]
        #self.VIDEO_ENTRADAS1 = 'H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4'
        #self.VIDEO_ENTRADAS2 = 'MPEG-2 vs H.264.mp4'
        #self.VIDEO_ENTRADAS3 = 'The Personal Computer Revolution- Crash Course Computer Science #25.mp4'
        self.VIDEO_ENTRADAS4 = 'video.mp4'
        #self.VIDEO_SAIDAS1 = 'convert-H.264 vs H.265 vs Mpeg2 vs Mpeg1.mp4'
        #self.VIDEO_SAIDAS2 = 'convert-MPEG-2 vs H.264.mp4'
        #self.VIDEO_SAIDAS3 = 'convert-The Personal Computer Revolution- Crash Course Computer Science #25.mp4'
        self.VIDEO_SAIDAS4 = 'convert-video.mp4'
        self.LOCAL_VIDEOS_SEM_ASPAS = '/home/mohammed/Área de trabalho/UFABC/2018/Q3 - 2018/AED-II/Projeto/Videos/'
        self.VIDEOS_ENTRADA_SEM_ASPAS = [#self.LOCAL_VIDEOS_SEM_ASPAS + VIDEO_ENTRADAS1,
                                         #self.LOCAL_VIDEOS_SEM_ASPAS + VIDEO_ENTRADAS2,
                                         #self.LOCAL_VIDEOS_SEM_ASPAS + VIDEO_ENTRADAS3,
                                         self.LOCAL_VIDEOS_SEM_ASPAS + self.VIDEO_ENTRADAS4]
        self.VIDEOS_SAIDA_SEM_ASPAS = [#self.LOCAL_VIDEOS_SEM_ASPAS + VIDEO_SAIDAS1,
                                       #self.LOCAL_VIDEOS_SEM_ASPAS + 'Videos-convertidos/' + VIDEO_SAIDAS2,
                                       #self.LOCAL_VIDEOS_SEM_ASPAS + VIDEO_SAIDAS3,
                                       self.LOCAL_VIDEOS_SEM_ASPAS + 'Videos-convertidos/' + self.VIDEO_SAIDAS4]
'''
    for i, num in enumerate(VIDEOS_ENTRADA):
        print(VIDEOS_ENTRADA[i])
'''
