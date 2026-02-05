import pygame
import sys

def show_menu(screen):
    font = pygame.font.SysFont("arial", 40)
    while True:
        screen.fill((0, 0, 0))

        start = font.render("Press ENTER to Start", True, (0, 255, 0))
        quit_game = font.render("Press Q to Quit", True, (255, 0, 0))

        screen.blit(start, (200, 200))
        screen.blit(quit_game, (220, 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()
