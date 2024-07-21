import pygame, random, sys, os

def draw_screen():
    display.fill ((screen_red,screen_green,screen_blue))
    ball_rect = pygame.draw.circle (display, (ball_red, ball_green, ball_blue), (ball_x,ball_y), ball_radius)
    pygame.draw.rect(display, left_player_color, pygame.Rect(left_player_x, left_player_y, left_player_width, left_player_height))
    pygame.draw.rect(display, right_player_color, pygame.Rect(right_player_x, right_player_y, right_player_width, right_player_height))

    left_score_text = score_font.render(str(left_player_score), True, (255,255,255))
    right_score_text = score_font.render(str(right_player_score), True, (255,255,255))
    display.blit(left_score_text,(0,0))
    display.blit(right_score_text,( width-right_score_text.get_width(),0))

def check_collisions():
    global ball_dx, ball_dy, left_player_score, right_player_score,ball_x ,ball_y
    
    if  (ball_x < left_player_x + left_player_width ):
        ball_dx = -ball_dx
        right_player_score += 1
        change_colors()
        reset_game()

    if (ball_x > width - ball_radius):
        ball_dx = -ball_dx
        left_player_score += 1
        change_colors()
        reset_game()

    #detect collision with top or bottom
    if ( (ball_y < ball_radius) or (ball_y>height-ball_radius) ):
        ball_dy = -ball_dy
        beep.play()
        change_colors()

    #detect ball collision with left player and adjust dx and dy
    if (ball_x-ball_radius <= left_player_x + left_player_width) and  (ball_y+ball_radius >= left_player_y) and (ball_y-ball_radius<= left_player_y+left_player_height):
        beep.play()
        diff = int(  ball_y - left_player_y - (left_player_height/2) )
            
        ball_dx = -ball_dx
            
        ball_dy = int(-ball_dy+(diff/5))
        
    #detect ball collision with right player
    if (ball_x+ball_radius >= right_player_x) and  (ball_y+ball_radius >= right_player_y) and (ball_y-ball_radius<= right_player_y+right_player_height):
        beep.play()
        diff = int(  ball_y - right_player_y - (right_player_height/2) )            
        ball_dx = -ball_dx
        ball_dy = int(-ball_dy+(diff/5))
            


def reset_game():
    global ball_x,ball_y, ball_dx,ball_dy
    ball_x = int(width/2)
    ball_y = int(height/2)
    ball_dx = random.randint(1,5)
    ball_dy = random.randint(1,5)
    

def move_objects():
    global ball_x,ball_y, left_player_y, right_player_y

    #move the ball
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    #detect keypresses and move players
    if keys[pygame.K_s]:
        left_player_y += 8
    if keys[pygame.K_w]:
        left_player_y -= 8
    if keys[pygame.K_UP]:
        right_player_y -= 8
    if keys[pygame.K_DOWN]:
        right_player_y += 8

    #do bounds checking on players
    if left_player_y < 0:
        left_player_y = 0
        
    if right_player_y < 0:
        right_player_y = 0

    if left_player_y> height-left_player_height:
        left_player_y = height-left_player_height

    if right_player_y> height-right_player_height:
        right_player_y = height-right_player_height
        
def change_colors():
    global screen_red, screen_green, screen_blue
    global ball_red, ball_green, ball_blue
    
    screen_red = random.randint(0,255)
    screen_green = random.randint(0,255)
    screen_blue = random.randint(0,255)

    ball_red = random.randint(0,255)
    ball_green = random.randint(0,255)
    ball_blue = random.randint(0,255)    


#==============================================================================#
# SETUP SECTION
#==============================================================================#

#set directory format
#os.chdir(os.path.dirname(__file__))
print(os.getcwd())

#screen variables
width = 1024
height = 768

#screen colors
screen_red = random.randint(0,255)
screen_green = random.randint(0,255)
screen_blue = random.randint(0,255)


#ball variables and properties
ball_dx = 3
ball_dy = 4
ball_x = 100
ball_y = 100
ball_radius = int( width/ 50 )
ball_red = random.randint(0,255)
ball_green = random.randint(0,255)
ball_blue = random.randint(0,255)

#player variables and properties

left_player_x = 20
left_player_y = int(height/2)
left_player_color = (255,128,64)
left_player_width = width/35
left_player_height = height/10
left_player_score = 0

right_player_width = width/35
right_player_height = height/10
right_player_x = width-20-right_player_width
right_player_y = int(height/2)
right_player_color = (64,128,255)
right_player_score = 0


#setup and initialize pygame
pygame.mixer.pre_init(44100, -16, 2, 1024*4)
pygame.init()
pygame.key.set_repeat(1, 10)
pygame.font.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode( (width,height), pygame.SRCALPHA, 32)

#load sounds 
beep = pygame.mixer.Sound("beep1.wav")
#bloop = pygame.mixer.Sound('./bloop.wav')

#setup fonts
score_font = pygame.font.SysFont('Comic Sans MS', 30)

reset_game()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
            

    move_objects()
    check_collisions() 
    draw_screen()
    pygame.display.flip()
    
