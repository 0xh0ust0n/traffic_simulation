# global packages
import pygame
import time

# custom packages
from car import Car
from human import Human
from traffic_light import Light
from config import Config, get_color

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
    
    # config for horizontal cars
    horizontal_cars = [    
        # left car turn
        {
            'flip_x'   : True,
            'flip_y'   : False,
            'rotate'   : 0,
            'scale'    : 1,
            'position' : (0, config.get_height() / 2 - 20 ),
            'x_update' : movement_speed,
            'y_update' : movement_speed * 0,
            'turn' : True,
            'turn_position': (config.get_width() / 2 + 75, config.get_height() / 2 - 20)
        },
         # left car straight
        {
            'flip_x'   : True,
            'flip_y'   : False,
            'rotate'   : 0,
            'scale'    : 1,
            'position' : (0, config.get_height() / 2 + 50 ),
            'x_update' : movement_speed,
            'y_update' : movement_speed * 0,
            'turn' : False
        },

      # right car straight
        {
            'flip_x'   : False,
            'flip_y'   : True,
            'rotate'   : 0,
            'scale'    : 1,
            'position' : (config.get_width() - 50, config.get_height() / 2 - 110),
            'x_update' : movement_speed * -1,
            'y_update' : movement_speed * 0,
            'turn' : False
        },
        # right car turn
        {
            'flip_x'   : False,
            'flip_y'   : True,
            'rotate'   : 0,
            'scale'    : 1,
            'position' : (config.get_width()- 150, config.get_height() / 2 - 30),
            'x_update' : movement_speed * -1,
            'y_update' : movement_speed * 0,
            'turn' : True,
            'turn_position': (config.get_width() / 2, config.get_height() / 2 - 30)

        },
    ]

    # config for vertical cars
    vertical_cars = [
        # top car turn
        {
            'flip_x' : False,
            'flip_y' : True,
            'rotate' : 90,
            'scale' : 1,
            'position' : (config.get_width() / 2 - 40, 0),
            'x_update' : movement_speed * 0,
            'y_update' : movement_speed,
            'turn' : True,
            'turn_position': (config.get_width() / 2 - 40, config.get_height() / 2 + 55)

        },
        # top car straight
        {
            'flip_x' : False,
            'flip_y' : True,
            'rotate' : 90,
            'scale' : 1,
            'position' : (config.get_width() / 2 - 140, 0),
            'x_update' : movement_speed * 0,
            'y_update' : movement_speed,
            'turn' : False
        },
        # bottom car straight
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 270,
            'scale' : 1,
            'position' : (config.get_width() / 2 + 75, config.get_height() - 150),
            'x_update' : movement_speed * 0,
            'y_update' : movement_speed * -1,
            'turn' : False
        },
        # bottom car turn
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 270,
            'scale' : 1,
            'position' : (config.get_width() / 2 - 30, config.get_height() - 150),
            'x_update' : movement_speed * 0,
            'y_update' : movement_speed * -1,
            'turn' : True,
            'turn_position': (config.get_width() / 2 - 30, config.get_height() / 2 - 50)

        }              
    ]

    # config for humans
    humans = [
        # bottom left human
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (295, config.get_height()-235),
            'x_update' : human_movement_speed * 0,
            'y_update' : human_movement_speed * -1
        },
        # top left human
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (295,180),
            'x_update' : human_movement_speed,
            'y_update' : human_movement_speed * 0
        },
        # top right human
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 3,
            'position': (config.get_width() - 350, 185),
            'x_update' : human_movement_speed * 0,
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
            'y_update' : human_movement_speed * 0
        },
      
    ]

    # config for the traffic lights
    traffic_lights = [
         # top left light
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 1.5,
            'position': (249,150),
            'light': "red",
            'clock' : 8
        },
        # top right light
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 1.5,
            'position': (config.get_width() - 303, 155),
            'light' : 'green',
            'clock' : 10
        },
        # bottom right light
        {
            'flip_x' : False,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 1.5,
            'position': (config.get_width()-306, config.get_height()-205),
            'light' : 'red',
            'clock' : 8
        },
        # bottom left light
        {
            'flip_x' : True,
            'flip_y' : False,
            'rotate' : 0,
            'scale' : 1.5,
            'position': (251, config.get_height()-205),
            'light': 'green',
            'clock' : 10

        }
    ]

    # sprite group for horizontal cars
    horizontal_car_sprites = pygame.sprite.Group()

    # sprite group for vertical cars
    vertical_car_sprites = pygame.sprite.Group()

    # sprite group for humans
    human_sprites = pygame.sprite.Group()
    
    # sprite group for traffic lights
    traffic_light_sprites = pygame.sprite.Group()

    # create car object for horizontal cars and add to group
    for car in horizontal_cars:
        car = Car(config = config, car_config=car)
        horizontal_car_sprites.add(car)

    # create car object for vertical cars and add to group
    for car in vertical_cars:
        car = Car(config = config, car_config = car)
        vertical_car_sprites.add(car)

    # create human object and add to group
    for human in humans:
        human = Human(config=config, human_config=human) 
        human_sprites.add(human)

    # create traffi light object and add to group
    for traffic_light in traffic_lights:
        traffic_light = Light(config=config, light_config=traffic_light)
        traffic_light_sprites.add(traffic_light)

    # update loop
    while running:

            # quit events to stop game
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False
        
            # get the current status of each traffic light
            current_lights = []
            for traffic_light_sprite in traffic_light_sprites:
                current_lights.append(traffic_light_sprite.get_light())

            # move vertical cars and stop horizontal
            # move human from bottom left to top left 
            # move human from top right to bottom right
            if current_lights[0] == 'green' and current_lights[2] == 'green':
                
                # config for horizontal cars
                for car in horizontal_car_sprites:
                    car.set_light('red')

                # config for vertical cars
                for car in vertical_car_sprites:
                    car.set_light('green')

                human_movement_speeds = [(0, human_movement_speed * -1), (0, 0), (0, human_movement_speed * 1 ), (0, 0)]

            # move horizontal cars and stop vertical
            # move human from top left to top right 
            # move human from bottom right to bottom left
            elif current_lights[1] == 'green' and current_lights[3] =='green': 

                # config for horizontal cars
                for car in horizontal_car_sprites:
                    car.set_light('green')

                # config for vertical cars
                for car in vertical_car_sprites:
                    car.set_light('red')

                human_movement_speeds = [(0, 0), (human_movement_speed, 0), (0, 0), (human_movement_speed * -1, 0)]
            
            # update the movement speed of each human
            for index, human_sprite in enumerate(human_sprites):
                human_sprite.set_movement_speed(human_movement_speeds[index])

            # move the horizontal cars
            horizontal_car_sprites.update()

            # move the vertical cars
            vertical_car_sprites.update()

            # move humans
            human_sprites.update()

            # update traffic light
            traffic_light_sprites.update()

            # clear the background picture
            screen.blit(bg, bg.get_rect(), bg.get_rect())

            # update the background image and horziontal cars
            for index, horizontal_car_sprite in enumerate(horizontal_car_sprites):
                screen.blit(bg, horizontal_car_sprite.get_rect(), horizontal_car_sprite.get_rect())
                screen.blit(source = horizontal_car_sprite.surf, dest = horizontal_car_sprite.rect)

           # update the background image and vertical cars
            for index, vertical_car_sprite in enumerate(vertical_car_sprites):
                screen.blit(bg, vertical_car_sprite.get_rect(), vertical_car_sprite.get_rect())
                screen.blit(source = vertical_car_sprite.surf, dest = vertical_car_sprite.rect)

            for human_sprite in human_sprites:
                screen.blit(bg, human_sprite.get_rect(), human_sprite.get_rect())
                screen.blit(source = human_sprite.surf, dest = human_sprite.rect)

            for traffic_light_sprite in traffic_light_sprites:
                screen.blit(bg, traffic_light_sprite.get_rect(), traffic_light_sprite.get_rect())
                screen.blit(source = traffic_light_sprite.surf, dest = traffic_light_sprite.rect)
            
            # update display and set frame rate
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    screen, clock = setup()
    loop(screen=screen, clock=clock)

    pygame.quit()
