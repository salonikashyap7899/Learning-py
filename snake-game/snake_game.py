import pygame
import sys
import random

# -------------------
# STEP 1: Initialize pygame
# -------------------
pygame.init()

# -------------------
# STEP 2: Game window setup
# -------------------
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# -------------------
# STEP 3: Colors
# -------------------
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# -------------------
# STEP 4: Snake settings (OUTSIDE LOOP)
# -------------------
snake_pos = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50]
]

direction = "RIGHT"
change_to = direction

# -------------------
# STEP 5: Food settings
# -------------------
food_pos = [
    random.randrange(1, width // 10) * 10,
    random.randrange(1, height // 10) * 10
]
food_spawn = True

# -------------------
# STEP 6: Score
# -------------------
score = 0

def show_score():
    font = pygame.font.SysFont("arial", 20)
    score_surface = font.render(f"Score : {score}", True, white)
    screen.blit(score_surface, (10, 10))

def game_over():
    font = pygame.font.SysFont("arial", 40)
    game_over_surface = font.render("GAME OVER", True, red)
    score_surface = font.render(f"Final Score : {score}", True, white)

    game_over_rect = game_over_surface.get_rect(center=(width/2, height/2 - 20))
    score_rect = score_surface.get_rect(center=(width/2, height/2 + 20))

    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)

    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# -------------------
# STEP 7: GAME LOOP
# -------------------
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        change_to = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        change_to = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        change_to = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        change_to = "RIGHT"

    direction = change_to

    # Move snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Snake growing logic
    snake_body.insert(0, list(snake_pos))

    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [
            random.randrange(1, width // 10) * 10,
            random.randrange(1, height // 10) * 10
        ]
    food_spawn = True

    # Drawing
    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Collision with wall
    if snake_pos[0] < 0 or snake_pos[0] > width - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over()

    # Collision with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score()
    pygame.display.update()
    clock.tick(10)
