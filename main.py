import pygame
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()

player = Player()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    key = pygame.key.get_pressed()
    player.press_key(key)

    screen.blit(player.surf, player.rect)
    pygame.display.flip()
