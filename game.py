# global packages
import pygame
import time

# custom packages
from car import Car
from human import Human
from config import Config

pygame.init()

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    
)

# screen config
config = None

# background picture
bg = None

# movement speed of the cars
movement_speed = 5

# movement speed of the human
human_movement_speed = 3



def setup():

    # create screen config class
    global config
    config = Config()
    
    # set up scren
    screen = pygame.display.set_mode(config.get_proportions())
    
    # get background image
    global bg
    bg = pygame.image.load("./assets/intersection.png").convert()
    
    print(f"Width: {bg.get_width()}; Height: {bg.get_height()}")

    # update the display size to background picture dimensions
    config.set_proportions(bg.get_width(), bg.get_height())
    screen = pygame.display.set_mode(config.get_proportions())
    
    # set up game clock for frame update
    clock = pygame.time.Clock()

    # add background picture to screen
    screen.blit(source = bg, dest = (0,0))

    return screen, clock

def loop(screen, clock):
    global config
    running = True
    
    # config for cars
    cars = [ 
        # left car
        {
            'flip_x'   : True,
            'flip_y'   : False,
            'rotate'   : 0,
            'scale'    : 2,
            'position' : (0, config.get_height() / 2 ),
            'x_update' : movement_speed,
            'y_update' : 0
        },
        # top car
        {
            'flip_x' : False,
            'flip_y' : True,
            'rotate' : 90,
            'scale' : 2,
            'position' : (config.get_width() / 2, 0),
            'x_update' : 0,
            'y_update' : movement_speed
        },
        # right car
        {
            'flip_x'   : False,
            'flip_y'   : True,
            'rotate'   : 0,
            'scale'    : 2,
            'position' : (config.get_width(), config.get_height() / 2 - 98),
            'x_update' : movement_speed * -1,
            'y_update' : 0
        },
        # bottom car
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 270,
            'scale' : 2,
            'position' : (config.get_width() / 2 - 98, config.get_height()),
            'x_update' : 0,
            'y_update' : movement_speed * -1
        }       
    ]

    # config for humans
    humans = [

        # top left human
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (295,180),
            'x_update' : human_movement_speed,
            'y_update' : 0
        },
        # top right human
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (config.get_width() - 350, 185),
            'x_update' : 0,
            'y_update' : human_movement_speed
        },
        # bottom right human
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (config.get_width()-350, config.get_height()-235),
            'x_update' : human_movement_speed * -1,
            'y_update' : 0
        },
        # bottom left human
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (295, config.get_height()-235),
            'x_update' : 0,
            'y_update' : human_movement_speed * -1
        },
    ]

    # sprite group for cars
    car_sprites = pygame.sprite.Group()

    # sprite group for humans
    human_sprites = pygame.sprite.Group()

    # create car object and add to group
    for car in cars:
        car = Car(config = config, car_config=car)
        car_sprites.add(car)

    # create human object and add to group
    for human in humans:
        human = Human(config=config, human_config=human) 
        human_sprites.add(human)

    # update loop
    while running:

            # quit events to stop game
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False
            
            # move the cars
            car_sprites.update()

            # move humans
            human_sprites.update()

            # clear the background picture
            screen.blit(bg, bg.get_rect(), bg.get_rect())

            # update the background image and cars
            for car_sprite in car_sprites:
                screen.blit(bg, car_sprite.get_rect(), car_sprite.get_rect())
                screen.blit(source = car_sprite.surf, dest = car_sprite.rect)

            for human_sprite in human_sprites:
                screen.blit(bg, human_sprite.get_rect(), human_sprite.get_rect())
                screen.blit(source = human_sprite.surf, dest = human_sprite.rect)

            # update display and set frame rate
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    screen, clock = setup()
    loop(screen=screen, clock=clock)

    pygame.quit()
