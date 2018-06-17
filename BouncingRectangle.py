
def draw_rectangle(screen,COLOR,x,y):
     pygame.draw.rect(screen, COLOR, [x, y, 50, 50])



import pygame
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
rect_x= 50.0
rect_y = 50.0
rectxSpeed=5
rectySpeed=5

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    string=str(rect_x)
    string2=str(rect_y)
    string3="["+string+"]"+"["+string2+"]"
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(string3,True,RED)
    screen.blit(text, [0, 0])    
    #Main rectangle
    draw_rectangle(screen,RED,rect_x,rect_y)
    #Second rectangle inside the rectangle 1
    rect_x += rectxSpeed
    rect_y+=rectySpeed
    if rect_y>450 or rect_y<0:
        rectySpeed=rectySpeed*-1
    if rect_x>650 or rect_x<0:
        rectxSpeed=rectxSpeed*-1

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(50)

# Close the window and quit.
pygame.quit()