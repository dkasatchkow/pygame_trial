# Simple pygame program
# Source: realpython.com/pygame-a-primer/

# Import and initiaize the pygame library
import pygame
import random

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

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,0,255))
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((10,10))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(
            center = (random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),random.randint(0,SCREEN_HEIGHT)))
        self.speed = random.randint(1,5)

    # Move the sprite based on speed
    # If the sprite goes off the edge of the screen, reset it randomly off the right edge
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Instantiate player. Right now this is just a rectangle
player = Player()

# Create a group to store enemies in
enemy_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

clock = pygame.time.Clock()

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

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemy_group.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player based on user keypresses
    player.update(pressed_keys)

    enemy_group.update()

    # Fill the background with white
    screen.fill((255,255,255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,0,255), (250,250), 40)

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50,50))

    # Give the surface a colour to separate it from the background
    surf.fill((0,0,0))
    rect = surf.get_rect()

    # Put the center of surf at the center of the screen
    surf_center = ((SCREEN_WIDTH-surf.get_width())/2, (SCREEN_HEIGHT-surf.get_height())/2)

    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, surf_center)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemy_group):
        print("You lose!")
        player.kill()
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit
pygame.quit()