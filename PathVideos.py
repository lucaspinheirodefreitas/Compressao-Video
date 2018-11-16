# # -*- coding: utf-8 -*-

class PathVideos(object):

    def __init__(self):
        self.VIDEO_ENTRADA = 'video'
        self.VIDEO_SAIDA = 'convert-video'
        self.LOCAL_VIDEOS = '/Videos/'
        self.VIDEOS_ENTRADA = []
        self.VIDEOS_SAIDA = []

    def new_path(self):
        numero_videos = input("Digite a quantidade de videos que deseja comprimir: ")
        for i in range(numero_videos):
            self.VIDEOS_ENTRADA.append(self.VIDEO_ENTRADA + str(i+1) + ".mp4")
            self.VIDEOS_SAIDA.append(self.VIDEO_SAIDA + str(i+1) + ".mp4")

'''
    for i, num in enumerate(VIDEOS_ENTRADA):
        print(VIDEOS_ENTRADA[i])
'''
