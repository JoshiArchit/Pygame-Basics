Filename : timer.py

--------------------------------------------------

Filename : sprite.py

<b>Notes : </b>
1. Pygame has its own key notations for handling events.<br>
eg) K_ESCAPE --> Key code for escape key

--------------------------------------------------

Filename : animated_sprites.py

<b>Notes -</b><br>
1. How animation works
- Set of sprites cycled on the screen in a sequence.
2. Animation Speed logic
- Increase the frame count slowly in decimals. 
- Thus instead of doing self.current_sprite += 1, increase in decimals like 0.2
- The frames get spread out and animation slows down (fps)


<b>Methods -</b>
1. pygame.display.set_caption() : Set window title
2. pygame.transform.scale(image,(screen_width, screen_height)) : Scale image 
   to screen size.