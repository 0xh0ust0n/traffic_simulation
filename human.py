import pygame

class Human(pygame.sprite.Sprite):
    def __init__(self, config, human_config = None, screen = None) -> None:
        super(Human, self).__init__()
        self.screen = screen
        self.config = config
        self.human_config = human_config

        # import an image and flip around Y and Y axis if needed
        image = pygame.transform.flip(pygame.image.load("./assets/human.png"), flip_x=self.human_config['flip_x'], flip_y=self.human_config['flip_y'])
        
        # rotate an image 
        image = pygame.transform.rotate(image, self.human_config['rotate'])
        self.surf = image.convert_alpha()

        # resize the image 
        self.surf = pygame.transform.smoothscale_by(self.surf, self.human_config['scale'])

        # place to the correct line
        self.rect = pygame.Rect(self.human_config['position'], (self.surf.get_size()))

    def update(self):
        
        # move the position of the human
        self.rect.move_ip(self.human_config['x_update'], self.human_config['y_update'])

        # check boundaries and update 
        if self.rect.left > self.config.get_width() - 350:
            self.rect.right = self.human_config['position'][0]
        
        if self.rect.top > self.config.get_height() - 235:
            self.rect.bottom = self.human_config['position'][1]

        if self.rect.right < 295 + self.surf.get_width():
            self.rect.left = self.human_config['position'][0]

        if self.rect.bottom < 180 + self.surf.get_height():
            self.rect.top = self.human_config['position'][1]

    # return the rectangle coordinates to draw
    def get_rect(self):
        return self.rect

    # set the X and Y movement speed of the human
    def set_movement_speed(self, speeds ):
        self.human_config['x_update'] = speeds[0]
        self.human_config['y_update'] = speeds[1]
        