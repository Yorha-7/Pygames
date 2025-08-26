# basic animations
import pygame 
from sys import exit
pygame.init()
x = 0
y = 0
add_x = 1
add_y = 1
clock = pygame.time.Clock()
screen = pygame.display.set_mode((318,159))
pygame.display.set_caption("Hello World!")
font = pygame.font.Font(None,50)
sky_surface = pygame.image.load('bg.png').convert_alpha()
text_surface = font.render('My Game', None, 'Green')
snail = pygame.Surface((50,50))
snail.fill("Blue")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
    clock.tick(60)
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(100,50))
    if x < 0:
        add_x = 1
    elif x > 318-50:
        add_x = -1
    if y < 0:
        add_y = 1
    elif y > 159-50:
        add_y = -1
    x = x + add_x
    y = y + add_y       
    screen.blit(snail,(x,y))
    
    pygame.display.update()