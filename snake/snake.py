import pygame
from pygame.locals import (
    KEYDOWN, QUIT,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE
)
import random

WIDTH = 50
HEIGHT = 26
SIZE = 16

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Snake(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.score = 0


class Apple(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y


def loop(screen, font, key_events, snake, apple):
  screen.fill(WHITE)

  # TODO: Add additional key presses here.
  if K_RIGHT in key_events:
    snake.x += 1

  # Draw the snake.
  pygame.draw.rect(screen, RED, [
    snake.x * SIZE,
    snake.y * SIZE, SIZE, SIZE])

  # Draw the apple.
  pygame.draw.circle(screen, GREEN, [
    apple.x * SIZE + SIZE/2, 
    apple.y * SIZE + SIZE/2], 8)

  # Draw the score.
  text_surface = font.render('Score: %d' % snake.score, False, BLACK)
  screen.blit(text_surface, (10, 10))



def run():
  # Set up pygame.
  pygame.init()

  # And set up drawing text.
  pygame.font.init()

  # Set up the screen.
  screen = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])

  # Choose a font.
  font = pygame.font.SysFont('Arial', 20)

  # Make a snake.
  snake = Snake(WIDTH/2, HEIGHT/2)

  apple = Apple(random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

  clock = pygame.time.Clock()
  while True:
    events = pygame.event.get()

    # Extract the key events.
    key_events = set([e.key for e in events if e.type == KEYDOWN])

    if e.type == QUIT:
      return

    # Update the screen.
    loop(screen, font, key_events, snake, apple)

    # Flip the display.
    pygame.display.flip()

    clock.tick(5)


if __name__ == '__main__':
  run()

