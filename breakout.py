import pygame
pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Game Over', False, (0, 0, 0))

screen = pygame.display.set_mode([500, 500])

running = True
green = (0, 255, 0)
blue = (0, 0, 255)

brick_row_count = 3
brick_column_count = 5
brick_width = 75
brick_height = 20
brick_padding = 10
brick_offset_top = 30
brick_offset_left = 30

bricks = []
for c in range(brick_column_count):
    bricks.append([])
    for r in range(brick_row_count):
        bricks[c].append({"x": 0, "y": 0})
       
# move it
def move_ball(ball_position_x, ball_position_y, ball_direction_x, ball_direction_y, paddle_pos_x):

    if ball_position_x + ball_direction_x >= 500 or ball_position_x + ball_direction_x <= 0:
        ball_direction_x = -ball_direction_x
        
    if ball_position_y + ball_direction_y <= 0:
        ball_direction_y = -ball_direction_y

    if ball_position_y == 460 and ball_position_x + 20 > paddle_pos_x and ball_position_x - 20 < paddle_pos_x + 70:
        ball_direction_y = -ball_direction_y
    elif ball_position_y + ball_direction_y + 10 >= 500:
        pygame.quit()


    return ball_position_x + ball_direction_x, ball_position_y + ball_direction_y, ball_direction_x, ball_direction_y

def move_paddle(paddle_x_position):
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT] and paddle_x_position > 10:
        return paddle_x_position - 10
    if pressed[pygame.K_RIGHT] and paddle_x_position < 430:
        return paddle_x_position + 10
    
    return paddle_x_position

def draw_bricks():
    for col in range(5):
        for ro in range(3):
            brick_x = (col*(brick_width+brick_padding))+brick_offset_left
            brick_y = (ro*(brick_height+brick_padding))+brick_offset_top
            bricks[col][ro] = {"x": (col*(brick_width+brick_padding))+brick_offset_left, "y": (ro*(brick_height+brick_padding))+brick_offset_top}
            pygame.draw.rect(screen, (0, 255, 0), (brick_x, brick_y, brick_width, brick_height))

def collision_detection(x, y, dy):
    print("BRICKS", bricks)
    for c in range(5):
        for r in range(3):
            print("LOOPING HERE", c, r)
            brick = bricks[c][r]
            print("HALLOOO", brick)
            if x > brick["x"] and x < brick["x"] + brick_width and y > brick["y"] and y < brick["y"] + brick_height: 
                return -dy
            return dy

def draw(running):
    # define ball positions 
    ball_x, ball_y = 250, 250
    direction_x, direction_y = 3, 3
    ball_radius = 20

    # define paddle positions
    paddle_width = 70
    paddle_x = 215


    while running:
        pygame.display.set_caption('BREAKOUT')

        # Fill the background with white
        screen.fill((255, 255, 255))

        # draw bricks
        draw_bricks()

        # check for collisions
        direction_y = collision_detection(ball_x, ball_y, direction_y)

        # draw paddle
        pygame.draw.rect(screen, (255, 255, 0), (paddle_x, 480, 50, 10))
        paddle_x = move_paddle(paddle_x)

        # draw ball
        pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)

        # change ball position and direction
        ball_x, ball_y, direction_x, direction_y = move_ball(ball_x, ball_y, direction_x, direction_y, paddle_x)

        # Flip the display
        pygame.display.flip()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# Done! Time to quit.
draw(running)
pygame.quit()