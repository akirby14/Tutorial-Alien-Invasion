"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the alien fleet and manages its behavior, including movement, collision detection, and rendering.
    Date Updated: 10/25/26
"""


import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    """ This class represents a fleet of aliens in the game. It manages the creation, movement, and 
    rendering of the alien fleet, as well as collision detection with other game elements."""

    def __init__(self, game: 'AlienInvasion'):

        """ Initializes the AlienFleet object."""

        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_diretion
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()


    def create_fleet(self):
        """ Creates a fleet of aliens based on the current game settings. """

        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)
            
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """ Creates a rectangular fleet of aliens based on the specified dimensions and offsets. """

        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col %2 == 0 or row %2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """ Calculates the offsets for positioning the alien fleet on the screen. """

        half_screen = self.settings.screen_h //2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """ Calculates the number of aliens that can fit in the fleet based on the screen dimensions and alien size. """

        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h / 2)//alien_h)

        if fleet_w % 2 ==0:
            fleet_w -= 1
        else:
            fleet_w -=2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)


    def _create_alien(self, current_x: int, current_y: int):
        """ Creates a single alien at the specified position and adds it to the fleet. """
        
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def check_fleet_edges(self):
        """ Checks if any alien in the fleet has reached the edge of the screen. If so, the fleet will drop down and change direction. """

        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """ Drops the entire alien fleet down by the specified drop speed. """

        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        """ Updates the position of the alien fleet and checks for edge collisions. """

        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """ Draws the alien fleet on the screen. """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """ Checks for collisions between the alien fleet and another sprite group. """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        """ Checks if any alien in the fleet has reached the bottom of the screen. """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        """ Checks if the alien fleet has been completely destroyed. """
        return not self.fleet