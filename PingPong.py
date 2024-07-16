# Import library
import pygame
import random
import copy

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 640
WINDOW_FPS = 144 # *WARNING* - Settings below 144hz will cause things to behave differently than intended.

# Color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("PingPong Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# FPS
fps = pygame.time.Clock()

# Game
running = True
time = 0
score = 0

# Ball
ball_size = 10
ball = [random.randrange(ball_size // 2, WINDOW_HEIGHT // 2 - ball_size // 2),
        random.randrange(ball_size // 2, WINDOW_WIDTH - ball_size // 2)]
ball_direction = [-2, 2]
ball_time = 0
ball_tick = 10

# Bar
bar = [WINDOW_HEIGHT - 20, WINDOW_WIDTH / 2]
bar_previous = bar
bar_size = 50
bar_direction = "none"
bar_time = 0
bar_tick = 5

# Main loop
while running:
    # Frame Per Second / Refresh Rate
    delta_time = fps.tick(WINDOW_FPS)
    time += delta_time

    # Key event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bar_direction = "left"
            if event.key == pygame.K_RIGHT:
                bar_direction = "right"
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bar_direction = "none"
            if event.key == pygame.K_RIGHT:
                bar_direction = "none"
            if event.key == pygame.K_SPACE:
                pass

    # Bar
    if time - bar_time >= bar_tick:
        bar_previous = copy.copy(bar)
        if bar_direction == "left":
            bar[1] += -2
        if bar_direction == "right":
            bar[1] += 2
        bar_time = time

    # Ball
    if time - ball_time >= ball_tick:
        ball[0] += ball_direction[0]
        ball[1] += ball_direction[1]
        ball_time = time

    if ball[1] <= (0 + ball_size / 2):
        ball[1] += 10
        ball_direction[1] *= -1
    if (WINDOW_WIDTH - ball_size / 2) <= ball[1]:
        ball[1] += -10
        ball_direction[1] *= -1
    if ball[0] <= (0 + ball_size / 2):
        ball[0] += 10
        ball_direction[0] *= -1

    if (bar[0] - ball_size / 2) <= ball[0] and ball[0] <= (bar[0] + 5 - ball_size / 2):
        if bar[1] <= ball[1] and ball[1] <= (bar[1] + bar_size):
            ball[0] += -10
            ball_direction[0] *= -1
            bar_delta = bar[1]-bar_previous[1]
            ball_direction[1] += bar_delta*0.5*random.random()
            score += 500
            if ball_tick > 0:
                ball_tick += -1

    # Game over
    if (WINDOW_HEIGHT - ball_size / 2) <= ball[0]:
        running = False

    # Refresh game screen
    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, [ball[1], ball[0]], ball_size / 2)
    pygame.draw.rect(window, GREEN, [bar[1], bar[0], bar_size, 5])
    window.blit(pygame.font.SysFont(None, 25).render(str(score), True, WHITE), (10, 10))
    pygame.display.update()

# Quit
print("Your score is : " + str(score))
pygame.quit()
quit()
