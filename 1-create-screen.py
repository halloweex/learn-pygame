import pygame
from random import randint

#Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


#Define the colors
WHITE = (255, 255, 255)
YELLOW = pygame.Color('yellow')
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

#define the clock
clock = pygame.time.Clock()

#Load the image
dragon_image = pygame.image.load('dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft= (0, 0)

#add the background music
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)

#Define the rectangle variables
rect_x = WINDOW_WIDTH//2 - 100
rect_y = WINDOW_HEIGHT//2 - 125
rect_width = 200
rect_height = 250

# define the flags for continuous movement
rect_is_moving_up = False
rect_is_moving_down = False
rect_is_moving_left = False
rect_is_moving_right = False

STEP = 10

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #     # continuous movement
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             rect_is_moving_left = True
    #         if event.key == pygame.K_RIGHT:
    #             rect_is_moving_right = True
    #         if event.key == pygame.K_UP:
    #             rect_is_moving_up = True
    #         if event.key == pygame.K_DOWN:
    #             rect_is_moving_down = True
    #
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_LEFT:
    #             rect_is_moving_left = False
    #         if event.key == pygame.K_RIGHT:
    #             rect_is_moving_right = False
    #         if event.key == pygame.K_UP:
    #             rect_is_moving_up = False
    #         if event.key == pygame.K_DOWN:
    #             rect_is_moving_down = False
    #
    # if rect_is_moving_left and rect_x >= STEP:
    #     rect_x -= STEP
    # if rect_is_moving_right and rect_x <= WINDOW_WIDTH - rect_width - STEP:
    #     rect_x += STEP
    # if rect_is_moving_up and rect_y >= STEP:
    #     rect_y -= STEP
    # if rect_is_moving_down and rect_y <= WINDOW_HEIGHT - rect_height - STEP:
    #     rect_y += STEP

    # Alternative way to make a continious movement
    # # Get a list of all keys currently being pressed down
    # keys = pygame.key.get_pressed()
    #
    # if keys[pygame.K_UP] and dragon_image_rect.y >= STEP:
    #     dragon_image_rect.y -= STEP
    # if keys[pygame.K_DOWN] and dragon_image_rect.y <= WINDOW_HEIGHT - rect_height - STEP:
    #     dragon_image_rect.y += STEP
    # if keys[pygame.K_LEFT] and dragon_image_rect.x >= STEP:
    #     dragon_image_rect.x -= STEP
    # if keys[pygame.K_RIGHT] and dragon_image_rect.x <= WINDOW_WIDTH - rect_width -STEP:
    #     dragon_image_rect.x += STEP

    # Fill the display surface to cover old images
    display_surface.fill(WHITE)

    #Draw a rectangle
    #pygame.draw.rect(display_surface, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    # Blit a surface objects at the given cordinates to our display
    display_surface.blit(dragon_image, dragon_image_rect)
    pygame.display.update()

    # Tick the clock LIKE FPS
    clock.tick(30)

# End the game
pygame.quit()