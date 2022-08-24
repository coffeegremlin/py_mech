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

# Say what you will about ES6 js but at least I don't have to tell it that the color red is red.
# Defining colors vvv (this is stupid)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# To do:
    # Define the game, mech, animation steps, font.
    # Load music and sounds
    # Load images, backgrounds, and spritesheets
    # Write some kind of function to psuedo animate drawing text
    # Write function to draw background and the GUI eg: the health bar and attacks
    #  Make two instances of mechs
    # Write a loop for the game to run
    # Add logic to quit the game (Don't trap your user in the game)