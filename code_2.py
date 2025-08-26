#dealing with fps
# diplaying lobjects on the window
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("The second test program")
clock = pygame.time.Clock()  # a clock object is created in here

test_surface = pygame.Surface((100,200))   # surface object created here
test_surface.fill('Red')                  # surface is colored in here 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(200,100))            # blit will layer the two surface one on other
    pygame.display.update()
    clock.tick(60)   # clock added here used to set max fps limit
