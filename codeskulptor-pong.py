# Codeskulptor Pong

import simplegui
import random

# screen globals
screen_width = 600
screen_height = 400

# ball globals
ball_radius = 20
ball_position = [screen_width / 2, screen_height / 2]
ball_velocity = [2, 2]

# paddle globals
paddle_width = 8
paddle_height = 80
half_paddle_width = paddle_width / 2
half_paddle_height = paddle_height / 2
paddle1_position = 40
paddle1_velocity = 0
paddle2_position = 40
paddle2_velocity = 0

# score globals 
score1 = 0
score2 = 0
    
# ball position and velocity
def ball_init(right):
    global ball_position, ball_velocity
    ball_position = [screen_width / 2, screen_height / 2]
    if right :
        ball_velocity = [random.randrange(3, 5),- random.randrange(3, 5)]
    else:
        ball_velocity = [- random.randrange(3, 5),- random.randrange(3, 5)]
       
def new_game():
    global paddle1_position, paddle2_position, paddle1_velocity, paddle2_velocity, score1, score2
    ball_init(True)
    score1 = 0
    score2 = 0
    paddle1_position = screen_height / 2
    paddle2_position = screen_height / 2
    paddle1_velocity = 0
    paddle2_velocity = 0
    
def draw(c):
    global score1, score2, paddle1_position, paddle2_position, ball_position, ball_velocity
 
    paddle1_position += paddle1_velocity
    paddle2_position += paddle2_velocity
    if paddle1_position >= screen_height - 40: 
        paddle1_position = screen_height - 40
    elif paddle1_position <= 40:
        paddle1_position = 40
    if paddle2_position >= screen_height - 40: 
        paddle2_position = screen_height - 40
    elif paddle2_position <= 40:
        paddle2_position = 40
        
    # draw mid line and gutters
    c.draw_line([screen_width / 2, 0],[screen_width / 2, screen_height], 1, "DarkOrchid")
    c.draw_line([paddle_width, 0],[paddle_width, screen_height], 1, "DarkOrchid")
    c.draw_line([screen_width - paddle_width, 0],[screen_width - paddle_width, screen_height], 1, "DarkOrchid")
    
    # draw paddles
    c.draw_line((0, paddle1_position - 40), (0, paddle1_position + 40), 16, "DarkOrchid")
    c.draw_line((screen_width, paddle2_position - 40), (screen_width, paddle2_position + 40), 16, "DarkOrchid")
    
    # update ball
    ball_position[0] +=1*ball_velocity[0]
    ball_position[1] +=1*ball_velocity[1]
    if ball_position[1] <= ball_radius:
        ball_velocity[1] =- ball_velocity[1]
    if ball_position[1] >= (screen_height - 1)- ball_radius:
        ball_velocity[1] =- ball_velocity[1]
    if ball_position[0] <= (paddle_width + ball_radius):
        if ball_position[1] < paddle1_position + 40 and ball_position[1] > paddle1_position - 40:
            ball_velocity[0] = - ball_velocity[0]
            ball_velocity[0] = 1.35*ball_velocity[0]
            ball_velocity[1] = 1.35*ball_velocity[1]
        else:
            ball_init(True)
            score2 +=1
        
    if ball_position[0] >= ((screen_width - 1)-(paddle_width + ball_radius)):
        if ball_position[1] < paddle2_position + 40 and ball_position[1] > paddle2_position-40:
            ball_velocity[0] =- ball_velocity[0]
            ball_velocity[0] = 1.1*ball_velocity[0]
            ball_velocity[1] = 1.1*ball_velocity[1]
        else:
            ball_init(False)
            score1 += 1

    # draw ball and scores
    c.draw_circle(ball_position, ball_radius, 5, "SlateBlue", "SlateBlue")
    c.draw_text(str(score1), [screen_width / 4, 60], 50, "BlueViolet")
    c.draw_text(str(score2), [screen_width / 1.4, 60], 50, "BlueViolet")
    
    if score1 == 10:
        c.draw_text("Player 1 Wins!", [65, 200], 80, 'MidnightBlue')
        ball_velocity[0] = 0
        ball_velocity[1] = 0
    if score2 == 10:
        c.draw_text("Player 2 Wins!", [65, 200], 80, 'MidnightBlue')
        ball_velocity[0] = 0
        ball_velocity[1] = 0

# keydown / keyup function
def keydown(key):
    global paddle1_velocity, paddle2_velocity
    if key == simplegui.KEY_MAP['W']:
        paddle1_velocity -= 8
    elif key == simplegui.KEY_MAP['S']:
        paddle1_velocity += 8
    elif key == simplegui.KEY_MAP['up']:
        paddle2_velocity -= 8
    elif key == simplegui.KEY_MAP['down']:
        paddle2_velocity += 8
def keyup(key):
    global paddle1_velocity, paddle2_velocity
    if key == simplegui.KEY_MAP['W']:
        paddle1_velocity = 4
    elif key == simplegui.KEY_MAP['S']:
        paddle1_velocity = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_velocity = 4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_velocity = 4

        
frame = simplegui.create_frame("Pong", screen_width, screen_height)
frame.set_canvas_background("PowderBlue")
button2 = frame.add_button("Restart", new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label("")
frame.add_label("Use W and S keys to move as Player 1")
frame.add_label("")
frame.add_label("Use UP and DOWN keys to move as Player 2")
frame.add_label("")
frame.add_label("First player to 10 points wins!")
frame.start()
