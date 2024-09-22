import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake parameters
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Food parameters
food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Score
score = 0

# Font for displaying score
font_style = pygame.font.SysFont(None, 25)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Game over flag
game_over = False

# Initial snake position (assuming it starts in the center)
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_change = 0  # Initial movement in x direction (can be 0 or snake_block)
snake_y_change = 0  # Initial movement in y direction (can be 0 or snake_block)
direction = "right"  # Initial direction (can be "left", "right", "up", or "down")

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Function to draw the food
def draw_food(food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

# Function to check for collisions
def check_collisions(snake_head, snake_list):
    # Check if snake has collided with itself
    for x in snake_list[:-1]:
        if x == snake_head:
            return True

    # Check if snake has collided with the screen boundaries
    if snake_head[0] < 0 or snake_head[0] >= screen_width or snake_head[1] < 0 or snake_head[1] >= screen_height:
        return True

    return False

def display_score(score):
    text = font_style.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
                snake_change = -snake_block
            elif event.key == pygame.K_RIGHT:
                direction = "right"
                snake_change = snake_block
            elif event.key == pygame.K_UP:
                direction = "up"
                snake_y_change = -snake_block
            elif event.key == pygame.K_DOWN:
                direction = "down"
                snake_y_change = snake_block

    # Update snake position based on direction and change values
    snake_x += snake_change
    snake_y += snake_y_change

    # Update snake head position
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    # Check if snake has eaten food
    if snake_head == [food_x, food_y]:
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length += 1
        score += 1

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for game over
    if check_collisions(snake_head, snake_list):
        game_over = True

    # Fill the screen with white color
    screen.fill(white)

    # Draw the snake, food, and score
    draw_snake(snake_block, snake_list)
    draw_food(food_x, food_y)
    display_score(score)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Game over message
font_style = pygame.font.SysFont(None, 50)
game_over_msg = font_style.render("Game Over", True, red)
game_over_x = (screen_width / 2) - game_over_msg.get_width() / 2
game_over_y = (screen_height / 2) - game_over_msg.get_height() / 2

while game_over:
    screen.fill(white)
    screen.blit(game_over_msg, [game_over_x, game_over_y])
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

# Quit Pygame
pygame.quit()
quit()
