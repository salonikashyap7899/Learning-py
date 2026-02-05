import pygame
import random
import sys

# ---------------- INIT ----------------
pygame.init()
pygame.mixer.init()

# ---------------- FULL SCREEN SETTINGS ----------------
# This detects your monitor's actual width and height
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Using FULLSCREEN and SCALED flags for best performance
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Snake Game Pro")
clock = pygame.time.Clock()

# ---------------- GAME SETTINGS ----------------
# Increased cell size so the snake isn't too small on high-res screens
CELL = 40 
START_SPEED = 7   # Slightly slower start for better control
MAX_SPEED = 25
speed = START_SPEED

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# ---------------- FONTS ----------------
font = pygame.font.SysFont("arial", 32, bold=True)
big_font = pygame.font.SysFont("arial", 72, bold=True)

# ---------------- LOAD ASSETS ----------------
try:
    grass = pygame.image.load("assets/grass.png").convert()
    # Scale background to match your monitor's resolution
    grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))
    
    food_img = pygame.image.load("assets/food.png").convert_alpha()
    food_img = pygame.transform.scale(food_img, (CELL, CELL))
    
    eat_sound = pygame.mixer.Sound("sounds/eat.wav")
    gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")
    pygame.mixer.music.load("sounds/bg.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"Error loading assets: {e}")

# ---------------- FUNCTIONS ----------------
def draw_background():
    screen.blit(grass, (0, 0))

def draw_snake():
    for i, block in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (block[0], block[1], CELL-2, CELL-2), border_radius=5)

def draw_ui():
    # Modern Score & Speed display
    score_text = font.render(f"Score: {score}", True, WHITE)
    speed_text = font.render(f"Speed: {int(speed)}", True, (0, 255, 255))
    screen.blit(score_text, (30, 30))
    screen.blit(speed_text, (30, 70))

def random_food():
    cols = WIDTH // CELL
    rows = HEIGHT // CELL
    while True:
        x = random.randint(0, cols - 1) * CELL
        y = random.randint(0, rows - 1) * CELL
        if [x, y] not in snake:
            return [x, y]

def move_snake():
    global score, speed, food_pos
    head_x, head_y = snake[0]

    if direction == "UP": head_y -= CELL
    elif direction == "DOWN": head_y += CELL
    elif direction == "LEFT": head_x -= CELL
    elif direction == "RIGHT": head_x += CELL

    new_head = [head_x, head_y]
    snake.insert(0, new_head)

    if new_head == food_pos:
        score += 1
        try: eat_sound.play()
        except: pass
        food_pos = random_food()
        # Speed increases every 2 points
        if score % 2 == 0 and speed < MAX_SPEED:
            speed += 1.0
    else:
        snake.pop()

def check_collision():
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    if head in snake[1:]:
        return True
    return False

def game_over_screen():
    pygame.mixer.music.stop()
    try: gameover_sound.play()
    except: pass

    while True:
        draw_background()
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        msg = big_font.render("GAME OVER", True, RED)
        sc = font.render(f"Final Score: {score}", True, WHITE)
        hint = font.render("Press 'R' to Restart | 'ESC' to Exit", True, WHITE)

        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 100))
        screen.blit(sc, (WIDTH//2 - sc.get_width()//2, HEIGHT//2))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 80))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

def run_game():
    global snake, direction, change_dir, score, speed, food_pos
    
    snake = [[CELL*5, CELL*5], [CELL*4, CELL*5], [CELL*3, CELL*5]]
    direction = "RIGHT"
    change_dir = "RIGHT"
    score = 0
    speed = START_SPEED
    food_pos = random_food()
    try: pygame.mixer.music.play(-1)
    except: pass

    while True:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Essential for Full Screen
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_UP and direction != "DOWN": change_dir = "UP"
                if event.key == pygame.K_DOWN and direction != "UP": change_dir = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT": change_dir = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT": change_dir = "RIGHT"

        direction = change_dir
        move_snake()

        if check_collision():
            game_over_screen()
            run_game()

        draw_background()
        screen.blit(food_img, (food_pos[0], food_pos[1]))
        draw_snake()
        draw_ui()
        pygame.display.update()

if __name__ == "__main__":
    run_game()