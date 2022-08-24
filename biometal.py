import pygame

class Biometal():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    # Need to add a sprite sheet, sound, and animation logic
    self.player = player
    self.size = data[0]
    self.offset = data[2]

# To do:
    # Load images, movement, maybe gravity logic (idk how fucking stupid python is inherently), animation update renders.
    # Add an attack and maybe a special attack logic