"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the bullet and manages its behavior, including movement and rendering.
    Date Updated: 10/20/26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):

    """ A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """ Initialize the bullet and set its starting position."""

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen."""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen."""
        
        self.screen.blit(self.image, self.rect)

