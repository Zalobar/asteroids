# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from pygame.locals import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # clock variable
    clock = pygame.time.Clock()
    dt = 0

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        


if __name__ == "__main__":
    main()
