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


snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomright = (600, 300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get(): #allows the user to exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #breaks the while loop, prevents conflict with pygame.init
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
    if game_active:
        #get screens onto respectinve cords from top left
        screen.blit(sky, (0, 0)) 
        screen.blit(ground,(0, 300))
        screen.blit(text, (320, 50))
        
        #snail
        snail_rect.x -= 4 #speed of snail moving

        if snail_rect.right <= 0:
            snail_rect.left = 800

        screen.blit(snail, snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False


    pygame.display.update()
    clock.tick(60) #ceiling frame rate