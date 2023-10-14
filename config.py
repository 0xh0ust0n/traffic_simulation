class Config():
    
    def __init__(self) -> None:
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 500

    def get_proportions(self):
        return (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def get_width(self):
        return self.SCREEN_WIDTH
    
    def get_height(self):
        return self.SCREEN_HEIGHT