import time
import pygame



#播放音乐的路径
filePath = ""

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()

#播放时长？
time.sleep(2)

#停止
pygame.mixer.music.stop()

