import pygame
from pygame import mixer
from mech import mech

mixer.init()
pygame.init()

# Game window goes here
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mecha')

# Add specific framerate logic
clock = pygame.time.Clock()
FPS = 60
# Might change it to 30 for retro feel later

