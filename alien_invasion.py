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
        #Use the codes below if you want the game screen to be displayed on full screen.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            self.ship.update()

            self._update_screen()

            #Set the games default framerate.
            self.clock.tick(60)

    def _check_events(self):
        """Watch and respond for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)


    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            #Move the ship to the left.
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_event(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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