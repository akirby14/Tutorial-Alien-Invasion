"""
    Program Name: Alien Invasion
    Author: Adryiana Kirby
    Purpose: This file creates the game statistics and manages its behavior, including score tracking, level progression, and saving high scores.
    Date Updated: 11/9/26
"""

# from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    
    """ A class to manage game statistics and track the player's progress."""

    def __init__(self, game: 'AlienInvasion'):
        """ Initialize the game statistics and set default values."""

        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """ Initialize the saved scores from a file or set to default if the file doesn't exist."""

        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """ Save the current high score to a file."""

        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """ Reset the game statistics to their initial values."""

        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """ Update the game statistics based on collisions and other events."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """ Update the maximum score if the current score exceeds it."""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """ Update the high score if the current score exceeds it."""
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        """ Update the score based on the number of aliens hit in collisions."""

        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """ Update the level when the player clears a wave of aliens."""

        self.level += 1