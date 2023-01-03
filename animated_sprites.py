"""
Filename : animated_sprites.py
Author : Archit Joshi
Description : Demonstration of sprite animations and other PyGame Basics
Language : Python 3.11
Assets : https://opengameart.org/content/opp2017-sprites-characters-objects-effects
Version : v1.3
Revisions :
v1.0 - Basic window setup and image import
v1.1 - Scaling image to screen size
v1.2 - Added update() and animate() methods
v1.3 - Slowed down animation and fps (check Notes.md)

"""

import sys

import pygame


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        for i in range(1, 11):
            item = pygame.image.load(f"sprites/frog/attack_{i}.png")
            item = pygame.transform.scale(item, (400, 200))
            self.sprites.append(item)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.is_animating is True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

    def animate(self):
        self.is_animating = True


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                player.animate()

    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
