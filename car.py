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
        self.surf = self.set_image()

        # place to the correct line
        self.rect = pygame.Rect(self.car_config['position'], (self.surf.get_size()))

        # to indicate whether the car has to turn or not
        self.turn = self.car_config['turn']

        # the degree of turning
        self.degree = 90
        # print(self.surf.get_size())

    def update(self):
        
        if self.turn == True:
            if self.rect.right >= self.config.get_width() / 2:
                self.surf = self.set_image(turn = True)
                self.turn = not self.turn

                car_config = self.car_config.copy()

                print(f"X_update: {self.car_config['x_update']}, Y_update: {self.car_config['y_update']}")

                car_config['y_update'] = self.car_config['x_update']
                car_config['x_update'] = self.car_config['y_update']

                print(f"X_update: {self.car_config['x_update']}, Y_update: {self.car_config['y_update']}")

                self.car_config = car_config
                # self.car_config['x_update'], self.car_config['y_update'] = self.car_config['y_update'], self.car_config['x_update']
            else: 
                self.rect.move_ip(self.car_config['x_update'], self.car_config['y_update'])

        else:
                # move the position of the car
                self.rect.move_ip(self.car_config['x_update'], self.car_config['y_update'])

        # check boundaries and update 
        if self.rect.left > self.config.get_width():
            self.rect.right = 0
            self.surf = self.set_image(turn = False)
            self.turn = not self.turn
             

        if self.rect.top > self.config.get_height():
            self.rect.bottom = 0
            self.surf = self.set_image(turn = False)
            self.turn = not self.turn

        if self.rect.right < 0:
            self.rect.left = self.config.get_width()
            self.surf = self.set_image(turn = False)
            self.turn = not self.turn


        if self.rect.bottom < 0:
            self.rect.top = self.config.get_height()
            self.surf = self.set_image(turn = False)
            self.turn = not self.turn


    # return the rectangle coordinates to draw
    def get_rect(self):
        print(self.rect)
        print("----------------")

        return self.rect

    # set the X and Y movement speed of the car
    def set_movement_speed(self, speeds):
        
        if speeds[0] != self.car_config['x_update'] or speeds[1] != self.car_config['y_update']:
            self.rect.left = self.car_config['position'][0] 
            self.rect.top = self.car_config['position'][1]

            self.rect.top = self.rect.top - self.car_config['position'][0] / 2
            if self.rect.bottom >= self.config.get_height():
                print(True)

            self.rect.width = self.rect.top - self.surf.get_width() / 2
            if self.rect.left >= self.config.get_width():
                print(True)

            self.rect = pygame.Rect(self.car_config['position'], (self.surf.get_size()))

            self.car_config['x_update'] = speeds[0]
            self.car_config['y_update'] = speeds[1]

    # set color
    def set_image(self, turn = None):
        # import an image and flip around Y axis (Keep y and change X's)
        image = pygame.transform.flip(pygame.image.load("./assets/car.png"), flip_x=self.car_config['flip_x'], flip_y=self.car_config['flip_y'])

        # rotate an image
        if turn:
            image = pygame.transform.rotate(image, 270)
        else:
            image = pygame.transform.rotate(image, self.car_config['rotate'])
        colors = get_color()
        image.fill(color=colors, special_flags=pygame.BLEND_MULT)

        surf = image.convert_alpha()

        # resize the image
        surf = pygame.transform.smoothscale_by(surf, self.car_config['scale'])

        return surf
