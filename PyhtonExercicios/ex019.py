#Faça um programa em python que reproduza o áudio de um ariquivo MP3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex019.mp3')
pygame.mixer.music.play()
pygame.event.wait()
