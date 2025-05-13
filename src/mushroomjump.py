import pygame
import random

pygame.init()

win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pink Mushroom Jump")

clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
pink = (255, 102, 180)
lightPink = (255, 190, 200)
brown = (150, 75, 0)
black = (0, 0, 0)
green = (34, 140, 35)
sky = (130, 200, 250)


ground_y = 360


x, y = 100, 310
w, h = 50, 50
velocity = 0
isJumping = False
gravity = 1
jump_power = -20


obstacles = []
obs_width = 50
obs_height = 50
obs_speed = 5


font = pygame.font.SysFont(None, 90)
game_over = False
run = True

while run:
    win.fill(sky)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if not game_over and event.key == pygame.K_SPACE:
                if not isJumping:
                    velocity = jump_power
                    isJumping = True
            elif game_over and event.key == pygame.K_r:
             
                y = ground_y - h
                velocity = 0
                isJumping = False
                obstacles.clear()
                game_over = False

    if not game_over:
      
        velocity += gravity
        y += velocity
        if y >= ground_y - h:
            y = ground_y - h
            isJumping = False

       
        if not obstacles or obstacles[-1].x < 600:
            height = random.randint(30, 100)
            new_obstacle = pygame.Rect(850, ground_y - height, obs_width, height)
            obstacles.append(new_obstacle)

   
        for obs in obstacles:
            obs.x -= obs_speed

     
        obstacles = [obs for obs in obstacles if obs.right > 0]

  
        player_rect = pygame.Rect(x, y, w, h)
        for obs in obstacles:
            if player_rect.colliderect(obs):
                game_over = True

 
        pygame.draw.ellipse(win, pink, (x, y, w, h))
        pygame.draw.rect(win, lightPink, (x + 10, y + 30, 30, 20))

   
        for obs in obstacles:
            pygame.draw.rect(win, brown, obs)

     
        pygame.draw.rect(win, green, (0, ground_y, 800, 40))
        for i in range(0, 800, 20):
            pygame.draw.line(win, black, (i, ground_y), (i, ground_y + 10), 2)
    else:
        text = font.render("GAME OVER", True, pink)
        win.blit(text, (400 - text.get_width() // 2, 200))

    pygame.display.update()
    clock.tick(FPS)