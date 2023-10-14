# global packages
import pygame
import time

# custom packages
from car import Car
from config import Config
pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    
)



def setup():
    
    config = Config()
    screen = pygame.display.set_mode(config.get_proportions())

    return screen

def loop(screen):
    running = True

    car = Car()
    
    while running:


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False
        
        screen.fill((255, 255, 255))

        surf = pygame.Surface((50, 50))

        surf.fill((0, 0, 0))
        rect = surf.get_rect()

        # screen.blit(source=car.surf, dest=(screen.get_width()/2-surf.get_width()/2, screen.get_height()/2 - surf.get_height()/2 ))

        screen.blit(source = car.surf, dest = car.rect)

        car.move()

        time.sleep(0.5)
        pygame.display.flip()

if __name__ == "__main__":
    screen = setup()
    loop(screen=screen)

    pygame.quit()
