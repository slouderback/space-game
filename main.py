import pygame
import random
from star import Star
from player import Player
from laser import Laser
from config import * 

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Game")
clock = pygame.time.Clock()

player = Player()
stars = []
lasers = []


def draw_screen():

    gameDisplay.fill((0,0,0))

    if random.randint(0, 100) > 60:
        stars.append(Star())

    for star in stars:
        if star.y > display_height:
            stars.remove(star)
            del star
            continue
        star.fall()
        pygame.draw.rect(gameDisplay, star.color, (star.x, star.y, star.width, star.height))

    for laser in lasers:
        if laser.y < 0:
            lasers.remove(laser)
            del laser
            continue
        laser.move_up()
        pygame.draw.rect(gameDisplay, laser.color, (laser.x, laser.y, laser.width, laser.height))

    pygame.draw.rect(gameDisplay, player.color, (player.x, player.y, player.width, player.height))
    

    



def main():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lasers.append(Laser(player))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_up()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move_down()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right()
        
        draw_screen()
        pygame.display.update()
        




if __name__ == '__main__':
    main()

