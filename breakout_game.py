# breakout_game
# Henry Roeser
# 5/14/25

import pygame
import random

# window dimensions and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Simple Breakout Game'
FPS = 30

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# font
FONT = 'arial'
FONT_SIZE_SCORE = 36
FONT_SIZE_START = 36
FONT_SIZE_INSTRUCTIONS = 24
FONT_SIZE_GAMEOVER_TITLE = 48
FONT_SIZE_GAMEOVER_SCORE = 36
FONT_SIZE_GAMEOVER_RESTART = 26

# player constants
PLAYER_WIDTH = 90
PLAYER_HEIGHT = 20
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT - 40
PLAYER_MOVEMENT_SPEED = 50

# ball constants
BALL_RADIUS = 10
BALL_DIAMETER = BALL_RADIUS * 2
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = SCREEN_HEIGHT // 2
BALL_INITIAL_X_SPEED = 10
BALL_INITIAL_Y_SPEED = 14

# brick constants
BRICK_WIDTH = 100
BRICK_HEIGHT = 30
BRICK_HORIZONTAL_PADDING = 50
BRICK_VERTICAL_PADDING = 20
BRICK_ROWS = 6
BRICK_COLUMNS = 8

class Player(pygame.sprite.Sprite):
    """Represents the player's paddle."""

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # position (x, y)
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.rect.center = (self.x, self.y)

    def update(self):
        """Moves the player based on keyboard input."""

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x <= SCREEN_WIDTH - PLAYER_WIDTH // 2 and self.y > SCREEN_HEIGHT - 100:
            self.x += PLAYER_MOVEMENT_SPEED
        if keys[pygame.K_LEFT] and self.x >= PLAYER_WIDTH // 2 and self.y > SCREEN_HEIGHT - 100:
            self.x -= PLAYER_MOVEMENT_SPEED

        self.rect.center = (self.x, self.y)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_image = pygame.Surface((BALL_DIAMETER, BALL_DIAMETER))
        pygame.draw.circle(ball_image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

        self.image = ball_image
        self.rect = self.image.get_rect()

        # position (x, y) and velocity
        self.x = BALL_START_X
        self.y = BALL_START_Y
        self.x_vel = BALL_INITIAL_X_SPEED
        self.y_vel = BALL_INITIAL_Y_SPEED
        self.rect.center = (self.x, self.y)

        def update(self):
            """Moves the ball and handles bouncing off walls."""
            self.x += self.x_vel
            self.y += self.y_vel

            if self.x <= BALL_RADIUS or self.x > SCREEN_WIDTH - BALL_RADIUS:
                self.x_vel *= -1 # reverse horizontal direction

            if self.y <= BALL_RADIUS:
                self.y_vel *= -1 # reverse horizontal direction

            self.rect.center = (self.x, self.y)


