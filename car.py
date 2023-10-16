import pygame
from pygame.locals import RLEACCEL
from config import Config

class Car(pygame.sprite.Sprite):
    def __init__(self, config, car_config = None, screen = None) -> None:
        super(Car, self).__init__()
        self.screen = screen
        self.config = config
        self.car_config = car_config

        # import an image and flip around Y axis (Keep y and change X's)
        image = pygame.transform.flip(pygame.image.load("./assets/car.png"), flip_x=self.car_config['flip_x'], flip_y=self.car_config['flip_y'])

        # rotate an image
        image = pygame.transform.rotate(image, self.car_config['rotate'])
        self.surf = image.convert_alpha()

        # resize the image
        self.surf = pygame.transform.smoothscale_by(self.surf, self.car_config['scale'])

        # place to the correct line
        self.rect = pygame.Rect(self.car_config['position'], (self.surf.get_size()))

        # print(self.surf.get_size())
    def update(self):
        
        # move the position of the car
        self.rect.move_ip(self.car_config['x_update'], self.car_config['y_update'])

        # check boundaries and update 
        if self.rect.left > self.config.get_width():
            self.rect.right = 0
        
        if self.rect.top > self.config.get_height():
            self.rect.bottom = 0

        if self.rect.right < 0:
            self.rect.left = self.config.get_width()

        if self.rect.bottom < 0:
            self.rect.top = self.config.get_height()

    # return the rectangle coordinates to draw
    def get_rect(self):
        return self.rect

        