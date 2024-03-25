import pygame as pygame
from Block import *

def drawScore(font):
    global score, lives
    
    text=font.render(str(score), True, white)
    window.blit(text, (200, 30))
    text=font.render(str(lives), True, white)
    window.blit(text, (600, 30))

def MoveBall():
    global lives, ballSpeedx, ballSpeedy, ballLocation, ball
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballLocation = [500, 300]
        lives = lives -1
        if lives == 0:
            ballSpeedx = 0
            ballSpeedy = 0
            lives = "Game Over"
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0) 
    
def MovePaddle():
    global PadASpeed, PadA
    """
    Moves the paddle side to side
    """
    
    if PadA.left <= 0:
        print("Left Side of Screen")
        PadA = PadA.move(2,0)
        PadASpeed = 0
    
    if PadA.right >= screenWidth:
        print("Right Side of Screen")
        PadA = PadA.move(-2,0)
        PadASpeed = 0
    #Add right of Paddle Code here
        
    PadA = PadA.move(PadASpeed, 0)
    pygame.draw.rect(window, white, PadA)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = -1
ballSpeedy = 1
black = (0,0,0)
white = (255, 255, 255)
radius = 20
ballLocation=[500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((500,570), (100,20))
PadASpeed = 0

score = 0
lives = 3

blocks = []

for i in range(10):
    aBlock = Block(window, i*100, 0)
    blocks.append(aBlock)

pygame.font.init()
#print(pygame.font.get_fonts())
font = pygame.font.SysFont(None, 72)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PadASpeed = -2
            if event.key == pygame.K_RIGHT:
                PadASpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                PadASpeed = 0
            if event.key == pygame.K_RIGHT:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedy = -ballSpeedy
        ballSpeedx = ballSpeedx + PadASpeed
    timer.tick(60)
    window.fill(black)
    for block in blocks:
        block.draw()
        if ball.colliderect(block.rect):
            blocks.remove(block)
            points = block.destroy()
            score = score + points
            ballSpeedy = -ballSpeedy
    MoveBall()
    MovePaddle()
    drawScore(font)
    pygame.display.flip()