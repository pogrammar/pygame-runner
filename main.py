from typing import Any
import pygame
from sys import exit

pygame.init()

#variables
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner sample')
clock = pygame.time.Clock() #Helps to set the ceiling frame rate
font = pygame.font.Font(None, 50)
game_active = True

sky = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/ground.png')
text = font.render('Runner', True, 'Black')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        def player_input(self):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gravity = -20
        def apply_gravity(self):
           self.gravity += 1
           self.rect.y += self.gravity

        def update(self):
            self.player_input()
            self.apply_gravity()

class Snail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        self.rect = self.image.get_rect(bottomright = (600, 300))

    def respawn(self):
        if self.rect.right <= 0:
            self.rect.left = 800


    def update(self):
        self.rect.x -= 6
        self.respawn()


snail = pygame.sprite.GroupSingle()
snail.add(Snail())
player = pygame.sprite.GroupSingle()
player.add(Player())


def collision():
    if pygame.sprite.spritecollide(player.sprite,snail,False):
        snail.empty()
        return False
    else: 
        return True





while True:
    for event in pygame.event.get(): #allows the user to exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #breaks the while loop, prevents conflict with pygame.init
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True


    if game_active:
        #get screens onto respectinve cords from top left
        screen.blit(sky, (0, 0)) 
        screen.blit(ground,(0, 300))
        screen.blit(text, (320, 50))
        
        snail.draw(screen)
        snail.update()

        player.draw(screen)
        player.update()

        game_active = collision()

    else:
        game_active = False
        screen.fill((94,129,162)) 
        gameover = font.render('Game Over - Press space to run', True, "Green")
        screen.blit(gameover, (220, 50))


    pygame.display.update()
    clock.tick(60) #ceiling frame rate