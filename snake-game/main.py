import pygame
import sys
import os

pygame.mixer.init()

eat_sound = pygame.mixer.Sound("sounds/eat.wav")
gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")
pygame.mixer.music.load("sounds/bg.mp3")
pygame.mixer.music.play(-1)

pygame.init()
pygame.mixer.init()
