# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

width = 1024
height = 768

# Set up the drawing window
screen = pygame.display.set_mode([width, height])

ball_x = int(width/2)
ball_y = int(height/2)
ball_radius = 75
ball_dx = 4
ball_dy = 6
clock = pygame.time.Clock()

screen.fill((255, 255, 255))
circle_rect=pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)
# Run until the user asks to quit
running = True
while running:
    clock.tick(120)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    #screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255,255,255),circle_rect )


    ball_x += ball_dx
    ball_y+=ball_dy

    if ball_x +ball_radius > width:
        ball_dx=-ball_dx

    if ball_x - ball_radius <=0:
        ball_dx=-ball_dx

    if ball_y - ball_radius <=0:
        ball_dy=-ball_dy

    if ball_y + ball_radius > height:
        ball_dy=-ball_dy
    
    # Draw a solid blue circle in the center
    circle_rect=pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)
    #print ("clock.tick:", clock.tick(self.fps))
    #print ("clock.get_fps", clock.get_fps())
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
