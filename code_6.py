# first test to the pid
# implementation of only proportionality constatnt in it
import pygame
from sys import exit
import time
pygame.init()
# variables
length,weidth = 2000,700
error,prev_error = 0,0
kp,ki,kd = 0.01,0,0.1
velocity = 1
clk = 60
cf = 0
setpoint = length - 100
pid_val = 0
curr_pos,prev_pos = 0,0
flag = 1


def pid():
    global cf,clk,kp,ki,kd,error
    prev_error = error
    error = setpoint - object_rect.x
    cf = kp*error + kd*(prev_error-error)
    prev_error = error
    return cf

def move_obj():
    global velocity
    object_rect.x += velocity
    return object_rect

# py objects and surfaces
font = pygame.font.Font(None,30)
text_frame = font.render('Finish',None,"Green")
screen = pygame.display.set_mode((length,weidth))
pygame.display.set_caption("Pid tester")
object_surface = pygame.Surface((2,2))
object_surface.fill('green')
object_rect = object_surface.get_rect(topleft = (0,weidth/2))
finish_surface = pygame.Surface((2,2))
finish_surface.fill('red')
finish_rect = finish_surface.get_rect(topleft = (setpoint,weidth/2))
clock = pygame.time.Clock()
screen.fill('black')

start_time = time.time()
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
    if object_rect.colliderect(finish_rect) and flag:
        time_text = font.render(f"{str(time.time()-start_time)} seconds",None,'Green')
        screen.blit(time_text,(0,0))
        flag = 0

    screen.blit(object_surface,object_rect)
    screen.blit(text_frame,(setpoint+2,weidth/2))         # gui for finish point
    screen.blit(finish_surface,finish_rect)               # dot to identify finish point
    
    clock.tick(clk)
    pygame.display.update()

