#first test to the pid
#implementation of only proportionality constatnt in it
import pygame
from sys import exit
pygame.init()
# variables
length,weidth = 800,700
error = 100
kp,ki,kd = 0.01,0,0
velocity = 1
clk = 60
cf = 0
setpoint = 800
pid_val = 0
curr_pos,prev_pos = 0,0
def pid():
    global cf,clk,kp,ki,kd,error
    error = setpoint - object_rect.x
    cf = kp*error
    return cf

def move_obj():
    global velocity
    object_rect.x += velocity
    return object_rect

#py objects and surfaces
screen = pygame.display.set_mode((length,weidth))
pygame.display.set_caption("Pid tester")
object_surface = pygame.Surface((2,2))
object_surface.fill('green')
object_rect = object_surface.get_rect(topleft = (0,350))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pid_val = pid_val + pid()
    prev_pos = object_rect.x
    object_rect.x += pid_val
    current_pos = object_rect.x
    if current_pos - prev_pos != 0:
        pid_val = 0
    screen.blit(object_surface,object_rect)
    clock.tick(clk)
    pygame.display.update()

