"""
Filename : sprite.py
Description : Sprite demonstration and pygame basics.
Reference : Clear Code Channel
Language : Python 3.11
Version : 1.2
Revisions :
v1.0 - Added basic setup and game loop logic
v1.1 - Added Crosshair class
v1.2 - Added Crosshair and background.

"""

import pygame
import sys
import random


# Inherit from Sprite
class Crosshair(pygame.sprite.Sprite):

    def __init__(self, cross_hair_path):
        super().__init__()
        self.image = pygame.image.load(cross_hair_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(
            "shooting-gallery-pack/Sounds/gunshot.wav")

    # Get position of crosshair from mouse position
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    # Simulate shooting
    def shoot(self):
        self.gunshot.play()


class Target(pygame.sprite.Sprite):
    def __init__(self, target_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(target_path)
        self.rect = self.image.get_rect()
        # Place targets at position (x,y)
        self.rect.center = [pos_x, pos_y]

def main():
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Game Screen
    screen_width = 1280
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.image.load(
        "shooting-gallery-pack/PNG/Stall/background.png")
    # Scale to fill screen
    background = pygame.transform.scale(background,
                                        (screen_width, screen_height))
    pygame.mouse.set_visible(False)

    # Crosshair
    crosshair = Crosshair(
        "shooting-gallery-pack/PNG/HUD/crosshair.png")
    # Create group for sprite so group can draw each sprite
    crosshair_group = pygame.sprite.Group()
    crosshair_group.add(crosshair)

    # Target
    target_group = pygame.sprite.Group()
    for target in range(20):
        target = Target("shooting-gallery-pack/PNG/Objects/target.png", random.randrange(0, screen_width), random.randrange(0,screen_height))
        target_group.add(target)

    # Game Loop
    while True:
        for event in pygame.event.get():
            # Quit on ESC
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Play gunshot sound when button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        pygame.display.flip()
        # Draw background, sprites
        screen.blit(background, (0, 0))
        crosshair_group.draw(screen)
        crosshair_group.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
