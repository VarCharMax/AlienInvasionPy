"""_summary_
"""

from typing import Literal
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')

        self.rect = self.image.get_rect()
        # These settings are probably redundant as they are immediately overwritten
        # by the calling function, but since they are used to define the x float property,
        # we keep them.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self) -> None | Literal[True]:
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        if self.rect.left <= 0:
            return True


    def update(self) -> None:
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self) -> None:
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
