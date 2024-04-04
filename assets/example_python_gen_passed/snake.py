import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS = 10

# Direction constants
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

# Snake properties
snake_pos = [[100, 50]]  # Initial position
snake_direction = RIGHT
snake_speed = 10

# Food
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True

# Score
score = 0

def draw_snake(snake_pos):
    """Draws the snake on the screen."""
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def move_snake(snake_pos, snake_direction):
    """Moves the snake in the current direction."""
    if snake_direction == UP:
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - 10])
    elif snake_direction == DOWN:
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + 10])
    elif snake_direction == LEFT:
        snake_pos.insert(0, [snake_pos[0][0] - 10, snake_pos[0][1]])
    elif snake_direction == RIGHT:
        snake_pos.insert(0, [snake_pos[0][0] + 10, snake_pos[0][1]])
    snake_pos.pop()

def check_collision(snake_pos):
    """Checks for collisions with boundaries, self, or food."""
    # Check boundary collision
    if snake_pos[0][0] >= SCREEN_WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT or snake_pos[0][1] < 0:
        return True
    # Check self collision
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            return True
    return False

def check_food_collision(snake_pos, food_pos):
    """Checks if the snake has collided with food."""
    if snake_pos[0] == food_pos:
        return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Movement controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move snake
    move_snake(snake_pos, snake_direction)

    # Check for collisions
    if check_collision(snake_pos):
        # Game over
        running = False

    # Check if snake eats food
    if check_food_collision(snake_pos, food_pos):
        score += 1
        food_spawn = False
        snake_pos.append(snake_pos[-1])

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
        food_spawn = True

    # Drawing
    screen.fill(BLACK)
    draw_snake(snake_pos)
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update display
    pygame.display.update()

    # Frame rate control
    clock.tick(FPS)

# Display final score
print(f"Final Score: {score}")