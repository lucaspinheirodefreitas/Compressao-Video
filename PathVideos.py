# # -*- coding: utf-8 -*-

class PathVideos(object):

    def __init__(self):
        self.VIDEO_ENTRADA = 'video'
        self.VIDEO_SAIDA = 'convert-video'
        self.VIDEOS_ENTRADA = []
        self.VIDEOS_SAIDA = []
        self.numero_videos = 0

    def new_path(self):
        self.numero_videos = input("Digite a quantidade de videos que deseja comprimir: ")
        for i in range(self.numero_videos):
            self.VIDEOS_ENTRADA.append(self.VIDEO_ENTRADA + str(i+1) + ".mp4")
            self.VIDEOS_SAIDA.append(self.VIDEO_SAIDA + str(i+1))

'''
    for i, num in enumerate(VIDEOS_ENTRADA):
        print(VIDEOS_ENTRADA[i])
'''
