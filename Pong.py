import pygame, sys
import random


# ball and player animations
def ball_animation():
    """ function that deals with the ball speed and the collision with either side of the screen width or screen height"""
    global ball_speed_x, ball_speed_y, player_1_score, player_2_score, game_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # check if ball is hitting left or right side
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
#    right paddle score
    if ball.left <= 0 :
        player_1_score += 1
        game_time = pygame.time.get_ticks()
#   left paddle score 
    if ball.right >= screen_width:
        player_2_score += 1
        game_time = pygame.time.get_ticks()
    
    # collision with paddle
    if ball.colliderect(right_paddle) and  ball_speed_x > 0:
            ball_speed_x *= -1
            play_pong()
    
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x *= -1
            play_pong()

def player_animation():
    right_paddle.y += player_speed
    if right_paddle.top <= 0:
        right_paddle.top = 0
    if right_paddle.bottom >= screen_height:
        right_paddle.bottom = screen_height
    


def player_2_animation():
  
    left_paddle.y += player_speed_2

    if left_paddle.top <= 0:
        left_paddle.top = 0
    if left_paddle.bottom >= screen_height:
        left_paddle.bottom = screen_height

def ball_respawn():
    """Subtracting the current time and  game time to slow down the pace after the respawn of the ball

    """
    global ball_speed_x, ball_speed_y, game_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - game_time < 700:
        start_counter_3 = score_font.render("3",False, ball_color)
        screen.blit(start_counter_3,(screen_width/2 - 10, screen_height/2 + 50))
    
    if 700 < current_time - game_time < 1400:
        start_counter_2 = score_font.render("2",False, ball_color)
        screen.blit(start_counter_2,(screen_width/2 - 10, screen_height/2 + 50))
    
    if 1400 < current_time - game_time < 2100:
        start_counter_1 = score_font.render("1",False, ball_color)
        screen.blit(start_counter_1,(screen_width/2 - 10, screen_height/2 + 50))
    
    
    if current_time - game_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    
    else:
        
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        game_time = None



def game_start_timer():
    pass


def play_pong():
    pygame.mixer.music.load(pong_sound)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)

def play_victory():
    pygame.mixer.music.load(victory_sound)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)


#setup
pygame.init()
pygame.mixer.init()
# this make the game runs at a constant speed
clock = pygame.time.Clock()

#setting main window
screen_width= 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pong_img = pygame.image.load("pong-image.ico")
pygame.display.set_caption("Pong")
pygame.display.set_icon(pong_img)

#timer
game_time = True

#sound setup
pong_sound = ("pong-sound.wav")
victory_sound = ("victory.mp3")

# colors
bg_color = ("#222222")
ball_color = ("#FFFFFF")
player_color = ("#EEE3CB")

#Scoreboard text and variables
player_1_score = 0
player_2_score = 0
score_font = pygame.font.SysFont("Ariel.ttf", 32)









#Game paddles
ball = pygame.Rect(screen_width/2 - 15 , screen_height/2 - 15,30,30,)
right_paddle= pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,155)
left_paddle = pygame.Rect(10, screen_height/2 -70, 10, 155)

#speed variables
ball_speed_x = 7
ball_speed_y = 7


# "player_speed" for right paddle, "player_speed_2" for left paddle
player_speed = 0
player_speed_2 = 0



while True:
    screen.fill(bg_color)
    #Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed_2 -= 7
            if event.key == pygame.K_s:
                player_speed_2 += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed_2 -= 7
            if event.key == pygame.K_s:
                player_speed_2 += 7
        

                
    
    #logic
    ball_animation()
    player_animation()
    player_2_animation()

    
    #Creating paddles and the ball
    pygame.draw.rect(screen, player_color, right_paddle)
    pygame.draw.rect(screen, player_color, left_paddle)
    pygame.draw.ellipse(screen,ball_color, ball)
    pygame.draw.aaline(screen, ball_color, (screen_width/2,0), (screen_width/2, screen_height))
    
    if game_time:
        ball_respawn()


    player_1_text = score_font.render(f"{player_1_score}",False,ball_color)
    screen.blit(player_1_text,(660,470))

    player_2_text = score_font.render(f"{player_2_score}",False,ball_color)
    screen.blit(player_2_text,(610,470))
    
    # winning screen, 3 is just for testing, it can be as many rounds as possible

    winning_font = pygame.font.SysFont("Ariel", 100)
    if player_1_score >= 3:
        play_victory()
        screen.fill(player_color)
        endscreen = winning_font.render("Player 1 won!!", True, ball_color)
        screen.blit(endscreen, (610, 470))
    
    if player_2_score >= 3:
        play_victory()
        screen.fill(player_color)
        endscreen = winning_font.render("Player 2 won!!", True, ball_color)
        screen.blit(endscreen, (610, 470))


    #update the window
    pygame.display.flip()
    clock.tick(60)
