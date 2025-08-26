#importing surface as image
#importing text on the game
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Code_3")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # a font as object is created in here

sky_surface = pygame.image.load('bg.png') # changed from just plane color to the image
text_surrface = test_font.render('My game',False, 'green')  # render the text by using the font be created, args = text,AA(anti aliasing),color
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surrface,(300,50))    # text is added as a surface in here 
    pygame.display.update()
