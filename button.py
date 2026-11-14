"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the button and manages its behavior, including rendering and click detection.
    Date Updated: 11/9/26
"""

import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    
    """ A class to manage buttons in the game."""

    def __init__(self, game: 'AlienInvasion', msg):
        """ Initialize the button and set its properties."""

        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0,0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """ Draw the button to the screen."""

        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """ Check if the button has been clicked."""

        return self.rect.collidepoint(mouse_pos)