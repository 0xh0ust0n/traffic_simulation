import pygame

class Light(pygame.sprite.Sprite):
    def __init__(self, config, light_config = None, screen = None) -> None:
        super(Light, self).__init__()
        self.screen = screen
        self.config = config
        self.light_config = light_config

        # convert the image and set it to the surface        
        self.surf = self.set_image()

        # place to the correct line
        self.rect = pygame.Rect(self.light_config['position'], (self.surf.get_size()))

        # light timer 
        self.clock = self.light_config['clock'] * 60
    
    def set_image(self):
        # import an image and flip around Y and Y axis if needed
        image = pygame.transform.flip(pygame.image.load(f"./assets/{self.light_config['light']}-light.png"), flip_x=self.light_config['flip_x'], flip_y=self.light_config['flip_y'])
        
        # rotate an image 
        image = pygame.transform.rotate(image, self.light_config['rotate'])

        surf = image.convert_alpha()

        # resize the image 
        surf = pygame.transform.smoothscale_by(surf, self.light_config['scale'])

        return surf
    
    def update(self):
        
        # countdown the light clock if not zero
        if self.clock != 0:
            self.clock = self.clock - 1

        # otherwise change the light
        else:
            if self.light_config['light'] == 'green':
                self.light_config['light'] = 'yellow'
                self.clock = 5 * 60
            elif self.light_config['light'] == 'red':
                self.light_config['light'] = 'green'
                self.clock = 8 * 60
            elif self.light_config['light'] == 'yellow':
                self.light_config['light'] = 'red'
                self.clock = 13 * 60

            # change the image
            self.surf = self.set_image()

    # return the rectangle coordinates to draw
    def get_rect(self):
        return self.rect

    # get current value of the light
    def get_light(self):
        return self.light_config['light']
        