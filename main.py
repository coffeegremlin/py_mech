import pygame
from pygame import mixer
from biometal import Biometal

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

# The game variables
start_count = 5
final_count = pygame.time.get_ticks()
round_complete = False
ROUND_COMPLETE_COOLDOWN_PERIOD = 3000
# Score of player1 and player2
fight_score = [0, 0]

# The Biometal variables
BIOMETAL_HX_SIZE = 160
BIOMETAL_HX_SCALE = 4
BIOMETAL_HX_OFFSET = [72, 56]
BIOMETAL_HX_DATA = [BIOMETAL_SCALE, BIOMETAL_SIZE, BIOMETAL_OFFSET]

# Biometal Fx Variables
BIOMETAL_FX _SIZE = 160
BIOMETAL_FX _SCALE = 4
BIOMETAL_FX _OFFSET = [113, 106]
BIOMETAL_FX _DATA = [BIOMETAL_FX_SCALE, BIOMETAL_FX_SIZE, BIOMETAL_FX_OFFSET]

# Set a background, might add a randomizer?
# Might set them to an array and use .random to pick one
# Also not sure how convertalpha is working, need to research
back_image = pygame.image.load("assets/images/backgrounds/humanbase5.png").convert_alpha()

biometal_hx_sheet = pygame.image.load("assets/images/Model-HX/")
biometal_fx_sheet = pygame.image.load("assets/images/Model-FX/")

# Need to add a victory effect maybe text or an image here

# Amount of steps in each animation frame from sheet
FX_ANIMATION_STEPS = []
HX_ANIMATION_STEPS = []