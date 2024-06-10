import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviors."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #Initialize clock for the games framerate.
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        #Create the game window by a set dimension and its title caption.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            self._update_screen

            #Set the games default framerate.
            self.clock.tick(60)

    def _check_events(self):
        """Watch and respond for keyboard and mouse events."""
        #Checks for any keydown event then respond to it accordingly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship tro the right
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
                    #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        #Redraw the ship during each pass through the loop
        self.ship.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()