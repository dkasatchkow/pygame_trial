# Simple pygame program
# Source: realpython.com/pygame-a-primer/

# Import and initiaize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Initialize
pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True
while running:

    # Did an event occur
    for event in pygame.event.get():

        # Was a key pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        # Was the event to leave the game
        elif event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255,255,255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,0,255), (250,250))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit
pygame.quit()