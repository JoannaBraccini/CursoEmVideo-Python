# Faça um programa em Python que abra e reproduza o áudio de um]
# arquivo mp3

import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("../samples/ambientembrace.mp3")
pygame.mixer.music.play()

pygame.event.wait()


#Solução foi igual, só não precisou do pygame.mixer.init()