import pygame
from pygame.locals import RLEACCEL
from config import Config

class Car(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Car, self).__init__()

        # import an image and flip around Y axis (Keep y and change X's)
        self.surf = pygame.transform.flip(pygame.image.load("./assets/car.png"), flip_x=True, flip_y=False).convert()
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def move(self):
        config = Config()
        self.rect.move_ip(20, 0)

        if self.rect.left > config.get_width():
            self.rect.right = 0



        