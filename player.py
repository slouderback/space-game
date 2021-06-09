import random
from config import * 


# pygame.draw.rect(gameDisplay, (0, 0, 255), ((display_width/2)-50, (display_height/2)+80, 100, 100))

class Player:

    def __init__(self):
        self.x = (display_width/2)-50
        self.y = (display_height/2)+80
        self.width = 100
        self.height = 100
        self.color = (0, 0, 255)

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5