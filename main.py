import pygame
import sys

def currentScore():
    currentTime=int((pygame.time.get_ticks()-startTime)/1000)
    return currentTime

def displayScore():
    currentTime=currentScore()
    scoreSur=testFont.render(f'SCORE:{currentTime}',False,'Blue')
    screen.blit(scoreSur,scoreSur.get_rect(midtop=(400,50)))
    

def scoreMenu():
    screen.fill((137, 207, 240))

    textPixelRunnerSurf=textFont.render('Pixel Runner',False,'Black')
    textPixelRunnerRect=textPixelRunnerSurf.get_rect(midtop=(400,50))

    screen.blit(textPixelRunnerSurf,textPixelRunnerRect)
    textScoreSurf=textFont.render(f'SCORE:{str(score)}',False,'Black')
    textScoreRect=textScoreSurf.get_rect(midtop=(400,300))
    screen.blit(textScoreSurf,textScoreRect)
    screen.blit(textplayAgainSurf,textPlayAgainRect)

    playerSurf=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
    
    playerRect=playerSurf.get_rect()
    playerSurf=pygame.transform.scale(playerSurf,(playerRect.w*2,playerRect.h*2))
    playerRect=playerSurf.get_rect(midtop=(400,100))
    screen.blit(playerSurf,playerRect)



pygame.init()
screen=pygame.display.set_mode((800,450))
pygame.display.set_caption('Roshan\'s game ')
clock=pygame.time.Clock()
testFont=pygame.font.Font('font/Pixeltype.ttf' ,50)

gameActive=True
startTime=0
score=0

textSurf=testFont.render('Score',False,'Black')
textRect=textSurf.get_rect(center=(400,40))

textFont=pygame.font.Font('font/Pixeltype.ttf' ,50)

textplayAgainSurf=textFont.render('Press Space to Play Again',False,'Black')
textPlayAgainRect=textplayAgainSurf.get_rect(midbottom=(400,430))



sky_surface=pygame.image.load('graphics/sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()

snail_surface=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(bottomright=(800,300))

player_surf=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(bottomright=(80,300))

time_per_frame=8690 #for 30fps
player_gravity=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            startTime=pygame.time.get_ticks()
            pygame.quit()
            sys.exit()
        if gameActive:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-20
        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print('space wes clicked !! ')
                    player_gravity=-20
        else :
            if event.type==pygame.MOUSEBUTTONDOWN and textPlayAgainRect.collidepoint(event.pos) : 
                gameActive=True
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                gameActive=True
            startTime=pygame.time.get_ticks()


    if gameActive:
        screen.blit(sky_surface,(0,0))
        pygame.draw.rect(screen,'Pink',textRect,0,5)
        pygame.draw.rect(screen,'Red',textRect,5)

        screen.blit(textSurf,textRect)
        
        screen.blit(ground_surface,(0,300)) 
        screen.blit(snail_surface,snail_rect)
    
        displayScore()
        player_gravity+=1
        player_rect.y=player_rect.y+player_gravity 
        if player_rect.bottom>=300:   
            player_rect.bottom=300
    
        screen.blit(player_surf,player_rect)
    
        snail_rect.x-=3

        if(snail_rect.x<1):
            snail_rect.x=800
    
        if snail_rect.colliderect(player_rect):
            score=currentScore()
            gameActive=False
            snail_rect.x=800

    else:
        scoreMenu()
        
 
    pygame.display.update()
    clock.tick(30)
