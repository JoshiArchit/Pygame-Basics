"""
Filename : sprite.py
Description : Sprite demonstration and pygame basics. Create a shooting game.
Reference : Clear Code Channel
Language : Python 3.11
Version : 1.3
Revisions :
v1.0 - Added basic setup and game loop logic.
v1.1 - Added Crosshair class.
v1.2 - Added Crosshair and background.
v1.3 - Added Targets and basic collision handling.
v1.4 - Adding multiple screens and levels. Moved all code from while to new
       class GameState and main_game()
v1.5 - Adding methods intro() & state_manager() to introduce a second screen

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
        pygame.sprite.spritecollide(crosshair, target_group, True)


class Target(pygame.sprite.Sprite):
    def __init__(self, target_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(target_path)
        self.rect = self.image.get_rect()
        # Place targets at position (x,y)
        self.rect.center = [pos_x, pos_y]


class GameState:
    def __init__(self):
        self.state = "intro"

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "main_game":
            self.main_game()

    def intro(self):
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Change state to main game on click and move to game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
            # Quit on hitting ESC key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Draw background, sprites
        screen.blit(background, (0, 0))
        screen.blit(ready_text,
                    (screen_width / 2 - 115, screen_height / 2 - 33))
        player_group.draw(screen)
        player_group.update()

        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Play gunshot sound when button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
            # Quit on hitting ESC key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Draw background, sprites
        screen.blit(background, (0, 0))
        target_group.draw(screen)
        player_group.draw(screen)
        player_group.update()

        pygame.display.flip()


# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Game Screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load(
    "shooting-gallery-pack/PNG/Stall/background.png")
# Scale to fill screen
background = pygame.transform.scale(background,
                                    (screen_width, screen_height))
ready_text = pygame.image.load("shooting-gallery-pack/PNG/HUD/text_ready.png")
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair(
    "shooting-gallery-pack/PNG/HUD/crosshair.png")
# Create group for sprite so group can draw each sprite
player_group = pygame.sprite.Group()
player_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    target = Target("shooting-gallery-pack/PNG/Objects/target.png",
                    random.randrange(0, screen_width),
                    random.randrange(0, screen_height))
    target_group.add(target)

# Game Loop
while True:
    game_state.state_manager()
    clock.tick(60)
