import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True


# move it
def move_ball(ball_position_x, ball_position_y, ball_direction_x, ball_direction_y):

    if ball_position_x + ball_direction_x >= 500 or ball_position_x + ball_direction_x <= 0:
        ball_direction_x = -ball_direction_x
        
    if ball_position_y + ball_direction_y >= 500 or ball_position_y + ball_direction_y <= 0:
        ball_direction_y = -ball_direction_y


    return ball_position_x + ball_direction_x, ball_position_y + ball_direction_y, ball_direction_x, ball_direction_y

def move_paddle(paddle_x_position):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return paddle_x_position - 10
            if event.key == pygame.K_RIGHT:
                return paddle_x_position + 10
    
    return paddle_x_position

def draw_bricks():
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, 50, 20))
    pygame.draw.rect(screen, (0, 255, 0), (110, 10, 50, 20))
    pygame.draw.rect(screen, (0, 255, 0), (220, 10, 50, 20))
    pygame.draw.rect(screen, (0, 255, 0), (330, 10, 50, 20))
    pygame.draw.rect(screen, (0, 255, 0), (440, 10, 50, 20))


def draw(running):
    # define ball positions 
    ball_x, ball_y = 250, 250
    direction_x, direction_y = 1, 1
    ball_radius = 20

    # define paddle positions
    paddle_width = 70
    paddle_x = 215


    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # draw bricks
        draw_bricks()

        # draw paddle
        pygame.draw.rect(screen, (255, 255, 0), (paddle_x, 480, 50, 10))
        paddle_x = move_paddle(paddle_x)

        # draw ball
        pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)

        # change ball position and direction
        ball_x, ball_y, direction_x, direction_y = move_ball(ball_x, ball_y, direction_x, direction_y)

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
draw(running)
pygame.quit()