import pygame
import random
from sys import exit
from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', ['x','y'])

pygame.init()  

# Constants
weidth = 800
height = 600
speed = 10
BLOCK_SIZE = 20
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 30)

class SnakeGame:
    def __init__(self, w=weidth, h=height):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT
        self.head = Point(self.w//2, self.h//2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - 2*BLOCK_SIZE, self.head.y)
        ]
        self.score = 0
        self.food = None
        self._place_food()
    
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. Collect input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        # 2. Move
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # 3. Check if game over
        if self._is_collision():
            return True, self.score

        # 4. Check if food eaten
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(speed)

        return False, self.score

    def _is_collision(self):
        # Hit walls
        if self.head.x >= self.w or self.head.x < 0 or self.head.y >= self.h or self.head.y < 0:
            return True
        # Hit itself
        if self.head in self.snake[1:]:
            return True
        return False

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = Point(x, y)

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()
        if game_over:
            break
    print(f"Final Score: {score}")
    pygame.quit()
