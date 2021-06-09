import random
from config import * 

class Star:

    def __init__(self):
        self.x = random.randrange(0, display_width)
        self.y = 0
        self.width = 3
        self.height = 1
        self.color = (255, 255, 255)

    def fall(self):
        self.y += 5

        if self.y > display_height:
            del self