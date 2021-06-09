from config import * 


# pygame.draw.rect(gameDisplay, (0, 0, 255), ((display_width/2)-50, (display_height/2)+80, 100, 100))

class Laser:

    def __init__(self, player):
        self.x = player.x + player.width/2 - 15/2
        self.y = player.y - player.height/2 + 30
        self.width = 15
        self.height = 50
        self.color = (255, 0, 0)

    def move_up(self):
        self.y -= 5