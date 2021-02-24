import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def press_key(self, key):
        if key[K_UP]:
            if self.rect.top < 0:
                self.rect.top = 0
            else:
                self.rect.move_ip(0, -1)
        if key[K_DOWN]:
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
            else:
                self.rect.move_ip(0, 1)
        if key[K_RIGHT]:
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            else:
                self.rect.move_ip(1, 0)
        if key[K_LEFT]:
            if self.rect.left < 0:
                self.rect.left = 0
            else:
                self.rect.move_ip(-1, 0)
