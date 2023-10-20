import random

class Config():
    
    def __init__(self, width = None, height = None) -> None:
        self.SCREEN_WIDTH = width or 500
        self.SCREEN_HEIGHT = height or 500

    def get_proportions(self):
        return (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def get_width(self):
        return self.SCREEN_WIDTH
    
    def get_height(self):
        return self.SCREEN_HEIGHT
    
    def set_proportions(self, width, height):
        self.SCREEN_HEIGHT = height
        self.SCREEN_WIDTH = width

def get_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)
    
