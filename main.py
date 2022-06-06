import pygame
import sys
from random import randint

def currentScore():
    currentTime=int((pygame.time.get_ticks()-startTime)/1000)
    return currentTime

def displayScore():
    score=currentScore()
    scoreSur=textFont.render(f'SCORE:{score}',False,'Blue')
    screen.blit(scoreSur,scoreSur.get_rect(midtop=(400,120)))
    return score
    
def scoreMenu():
    
    obstacleRectList.clear()
    # Pixel Runner Text 
    textPixelRunnerSurf=textFont.render('Pixel Runner',False,'Black')
    textPixelRunnerRect=textPixelRunnerSurf.get_rect(midtop=(400,50))

    #Sccore Text 
    textScoreSurf=textFont.render(f'SCORE:{str(score)}',False,'Black')
    textScoreRect=textScoreSurf.get_rect(midtop=(400,300))
    
    # Play again Text
    textplayAgainSurf=textFont.render('Press Space to Play Again',False,(251, 251, 253))
    textPlayAgainRect=textplayAgainSurf.get_rect(midbottom=(400,430))
    
    
    #Player Image
    playerSurf=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
    playerRect=playerSurf.get_rect()
    playerSurf=pygame.transform.scale(playerSurf,(playerRect.w*2,playerRect.h*2))
    playerRect=playerSurf.get_rect(midtop=(400,100))

    # display to screen

    screen.fill((137, 207, 240)) # main screen
    screen.blit(textPixelRunnerSurf,textPixelRunnerRect) # top Text
   
    screen.blit(textScoreSurf,textScoreRect) # Score Text
    screen.blit(playerSurf,playerRect)# Player Image
    screen.blit(textplayAgainSurf,textPlayAgainRect) # play Again text

def obstacleMovement(obstacleRectList):
    if obstacleRectList:
        for obstacleRect in obstacleRectList:
            obstacleRect.x-=5
            if(obstacleRect.bottom==300):
                screen.blit(snailSurf,obstacleRect)
            else:
                screen.blit(flySurf,obstacleRect)
        #delete obstacles as long as they leave screen
        obstacleRectList=[obstacleRect for obstacleRect in obstacleRectList if obstacleRect.x>-100]
        return obstacleRectList
    else:
        return []
        
def collions(player,obstacles):
    if obstacles:
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                return False
    return True


pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((800,450)) # main Screen 
pygame.display.set_caption('Roshan\'s game ')

textFont=pygame.font.Font('font/Pixeltype.ttf' ,50)
gameActive=True
startTime=0
score=0
time_per_frame=8690 #for 30fps
player_gravity=0

textSurf=textFont.render('Score',False,(251, 251, 253))
textRect=textSurf.get_rect(center=(400,40))

sky_surface=pygame.image.load('graphics/sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()

snailSurf=pygame.image.load('graphics/snail/snail1.png').convert_alpha()


flySurf=pygame.image.load('graphics/fly/fly1.png').convert_alpha()


player_surf=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(bottomright=(80,300))

obstacleRectList=[]

################
#   TIMERS
###############
obstacleTimer=pygame.USEREVENT+1
pygame.time.set_timer(obstacleTimer,1400)


################
#   EVENT LOOP
###############
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
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                gameActive=True
            startTime=pygame.time.get_ticks()
        if event.type==obstacleTimer and gameActive:
            if randint(0,2):
                obstacleRectList.append(snailSurf.get_rect(bottomright=(randint(900,1100),300)))
            else:
                obstacleRectList.append(flySurf.get_rect(bottomright=(randint(900,1100),210)))


    if gameActive:
        screen.blit(sky_surface,(0,0))
        pygame.draw.rect(screen,'Pink',textRect,0,5)
        pygame.draw.rect(screen,'Red',textRect,5)

        screen.blit(textSurf,textRect)
        
        screen.blit(ground_surface,(0,300)) 
        
    
        score=displayScore()
        #player
        player_gravity+=1
        player_rect.y=player_rect.y+player_gravity 
        if player_rect.bottom>=300:   
            player_rect.bottom=300
    
        screen.blit(player_surf,player_rect)

        #Obstacle movement
        obstacleRectList=obstacleMovement(obstacleRectList)
        
        # collsion
        
        gameActive=collions(player_rect,obstacleRectList)
        
    else:
        scoreMenu()
        
 
    pygame.display.update()
    clock.tick(60)
