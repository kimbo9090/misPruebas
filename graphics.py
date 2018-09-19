"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
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
    
    
    # ALL EVENT PROCESSING SHOULD GO BELOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type== pygame.KEYDOWN:
            print("PABAJO")
        
    #ALL EVENT PROCESSING SHOULD GO ABOCE       
 
    # --- Game logic should go BELOW
    # --- Game logic should go above
    
    
    # --- Drawing code should go below
    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Quieres 50 euros o no quieres 50 euros", True, BLACK)
    screen.blit(text, [200, 200])
    for x in range(0,100,20):
        pygame.draw.line(screen,GREEN,[x,0],[x,100],3)
        
        
    #draw a rectangle
    pygame.draw.rect(screen,BLACK, [150,50,250,100],5)
    #draw a elipse
    pygame.draw.ellipse(screen,BLACK, [150,50,250,100],5)
    #--- Drawing should go above
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()