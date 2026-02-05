import random

class Enemy:
    def __init__(self):
        self.x = random.randrange(0, 600, 20)
        self.y = random.randrange(0, 400, 20)

    def move(self):
        self.x += random.choice([-20, 20])
        self.y += random.choice([-20, 20])

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, 20, 20])
