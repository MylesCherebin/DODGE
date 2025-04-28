import pygame
import sys
from bullet import Bullet
from player import Player
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = Player(pos,10)
bullets = set()
used = set()
bt = 100

score = 0
background = pygame.Surface((screen.get_width(),64))
background = background.convert()
background.fill("white")
font = pygame.font.Font(None, 30)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    text = font.render('Score: ' + str(score),True,"black")
    textpos = text.get_rect(x=580,y=10)
    background.fill('white')
    background.blit(text, textpos)

    # send a bullet towards the player on every bt-th game loop
    if bt == 0:
        bull = Bullet(player.pos,random.randrange(0,screen.get_width()), random.randrange(0,screen.get_height()))
        bullets.add(bull)
        bt = 10
    else:
        bt -= 1

    pygame.draw.circle(screen, "black", player.pos, player.rad)
    
    for bullet in bullets:
        player.collision(bullet)
        pygame.draw.rect(screen,"black",bullet.rect)
        bullet.move()
        if (bullet.rect.top < 0 or bullet.rect.top > screen.get_height() 
            or bullet.rect.left < 0 or bullet.rect.left > screen.get_width() 
            or(bullet.rect.left == bullet.goal_x) and bullet.rect.top == bullet.goal_y):
            used.add(bullet)
        player.collision(bullet)
    for shell in used:
        if shell in bullets:
            bullets.remove(shell)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move_y( -300 * dt)   
    if keys[pygame.K_s]:
        player.move_y( 300 * dt) 
    if keys[pygame.K_a]:
        player.move_x( -300 * dt) 
    if keys[pygame.K_d]:
        player.move_x( 300 * dt) 

    screen.blit(background, (0,0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    score += 1
pygame.quit()