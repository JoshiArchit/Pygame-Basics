"""
Filename : timer.py
Description : Timer demonstration and pygame basics.
Reference : Clear Code Channel
Language : Python 3.11
Version : 1.0
"""

import pygame
import sys

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))  # 800*800 window
clock = pygame.time.Clock()  # timer object

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        # Handle case when player presses ESC
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Start recording time once a button is pressed
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            # Change color to white on button press (RGB color code)
            screen.fill((255, 255, 255))

    current_time = pygame.time.get_ticks()

    # Change back to black
    if current_time - button_press_time > 2000:
        screen.fill((0, 0, 0))

    print(
        f"Current Time : {current_time} Button Press Time : {button_press_time}")

    pygame.display.flip()
    clock.tick(60)
