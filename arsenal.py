"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the arsenal and manages its behavior, including firing bullets, and rendering them on the screen.
    Date Updated: 10/20/26
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """ A class to manage the player's arsenal of bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """ Initialize the arsenal and set its properties."""

        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """ Update the position of bullets and remove any that have gone off-screen."""

        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """ Remove bullets that have gone off the top of the screen."""

        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """ Draw all bullets in the arsenal to the screen."""

        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """ Fire a bullet if the limit has not been reached yet."""
        
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False