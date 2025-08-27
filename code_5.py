# animation by using rectangles
# collision detection
import pygame
from sys import exit
x = 0
y = 0
add_x = 1
add_y = 1

def move_obj():
    global add_x,add_y
    x,y = player_rect.topleft
    if x < 0:
        add_x = 1
    elif x > 318-20:
        add_x = -1
    if y < 0:
        add_y = 1
    elif y > 159 - 20:
        add_y = -1
    if player_rect.colliderect(object_rect):         # here collision is being checked
        add_x = (-add_x*2) + add_x
        add_y = (-add_y*2) + add_y
    
    return (x+add_x,y+add_y)

pygame.init()
screen = pygame.display.set_mode((318,159))
pygame.display.set_caption('Hello World!')
font = pygame.font.Font(None,30)

clock = pygame.time.Clock()
test_frame = pygame.image.load('bg.png').convert_alpha()
text_frame = font.render("My Game", None, 'Blue')
player_surf = pygame.Surface((20,20))
player_surf.fill('purple')
player_rect = player_surf.get_rect(topleft = (80,110)) #adding rectangle in here
object_surf = pygame.Surface((20,20))
object_surf.fill('red')
object_rect = object_surf.get_rect(topleft = (120,90)) #adding rectangle in here
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player_rect.topleft = move_obj() # updating rectangle position
    screen.blit(test_frame,(0,0))
    screen.blit(player_surf,player_rect) 
    screen.blit(object_surf,object_rect) 
    screen.blit(text_frame,(110,20))
    clock.tick(60)            
    pygame.display.update()