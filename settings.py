"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the settings and manages the game's configuration.
    Date Updated: 11/9/26
"""

from pathlib import Path
class Settings:

    """ A class to manage the game's settings and configuration."""

    def __init__(self):
        """ Initialize the game's settings and configuration."""

        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'scenebackground.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'slingshot.png'
        self.ship_w = 175
        self.ship_h = 175
        
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'stone.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'shoot.ogg'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'skill_hit.mp3'


        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'blackfly.gif'
        self.buzz_sound = Path.cwd() / 'Assets' / 'sound' / 'fly-buzz.mp3'
        self.alien_w = 50
        self.alien_h = 50
        self.fleet_diretion = 1
        
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255,255,255)
        self.button_font_size = 25
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Boldonse' / 'Boldonse-Regular.ttf'

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game."""

        self.ship_speed = 5
        self.starting_ship_count = 3
            
        self.bullet_w = 25
        self.bullet_h = 25 
        self.bullet_speed = 7 
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        """ Increase the game's difficulty by scaling the speed and point values."""

        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale