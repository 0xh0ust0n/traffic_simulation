import math
import pygame
from pygame.locals import RLEACCEL
from config import Config, get_color

class Car(pygame.sprite.Sprite):
    def __init__(self, config, car_config = None, screen = None) -> None:
        super(Car, self).__init__()
        self.screen = screen
        self.config = config
        self.car_config = car_config

        # convert the image and set it to the surface        
        self.surf = self.reset()

        # to indicate whether the car has to turn or not
        self.turn = self.car_config['turn']

        # the degree of turning
        self.degree = 90

        # current light of the traffic light for the car
        self.light = 'red'

        # x speed
        self.x_update = car_config['x_update']

        # y speed
        self.y_update = car_config['y_update']

    def update(self):
        
        # move if the light is green
        if self.light == "green":
            self.rect.move_ip(self.x_update, self.y_update)

        # if turn config is enabled
        if self.turn:
            
            # if the car is in the right area for turn 

            
            if abs(self.rect.left - self.car_config['position'][0]) > self.car_config['turn_position'][0] or abs(self.rect.top - self.car_config['position'][1]) > self.car_config['turn_position'][1]:
            # if self.rect.left in range(int(self.config.get_width() / 2 + 75 - 15), int(self.config.get_width() / 2 + 75 + 15) ):
                
                # disable turn configuration
                self.turn = not self.turn

                # rotate the car
                self.surf = pygame.transform.rotate(self.surf, 90)
                
                # update speed of the car
                self.x_update, self.y_update = self.y_update, -1 * self.x_update


        # check boundaries and update and reset the configuration
        if self.rect.left > self.config.get_width():
            self.surf = self.reset()
             
        if self.rect.top > self.config.get_height():
            self.surf = self.reset()

        if self.rect.right < 0:
            self.surf = self.reset()

        if self.rect.bottom < 0:
            self.surf = self.reset()


    # return the rectangle coordinates to draw
    def get_rect(self):

        return self.rect

    # reset the coordinates of car object
    def reset(self, degree = None):
        # import an image and flip around Y axis (Keep y and change X's)
        image = pygame.transform.flip(pygame.image.load("./assets/car.png"), flip_x=self.car_config['flip_x'], flip_y=self.car_config['flip_y'])

        # rotate the image
        image = pygame.transform.rotate(image, self.car_config['rotate'])

        # generate a color for the car
        colors = get_color()
        image.fill(color=colors, special_flags=pygame.BLEND_MULT)

        # create the surface
        surf = image.convert_alpha()

        # resize the image
        surf = pygame.transform.smoothscale_by(surf, self.car_config['scale'])

        # put car in the start coordinates
        self.rect = pygame.Rect(self.car_config['position'], (surf.get_size()))

        # assign turn status
        self.turn = self.car_config['turn']

        # reset speed configurations

        self.y_update = self.car_config['y_update']
        self.x_update = self.car_config['x_update']
        
        return surf

    def set_light(self, light):
        self.light = light

    def get_status(self):
        return self.status