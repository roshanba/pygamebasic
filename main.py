import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((800,450))
pygame.display.set_caption('Roshan\'s game ')
clock=pygame.time.Clock()
testFont=pygame.font.Font('font/Pixeltype.ttf' ,50)

def displayScore():
    currentTime=pygame.time.get_ticks()
    scoreSur=testFont.render(f'{currentTime}',False,'Blue')
    screen.blit(scoreSur,scoreSur.get_rect(center=(400,100)))

gameActive=True


textSurf=testFont.render('Score',False,'Black')
textRect=textSurf.get_rect(center=(400,40))

text_playAgain_font=pygame.font.Font('font/Pixeltype.ttf' ,50)
text_playAgain_surface=text_playAgain_font.render('Play Agaiin',False,'Black')
text_PlayAgain_rect=text_playAgain_surface.get_rect(center=(400,100))


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
            if event.type==pygame.MOUSEBUTTONDOWN and text_PlayAgain_rect.collidepoint(event.pos) : 
                gameActive=True
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                gameActive=True


    if gameActive:
        screen.blit(sky_surface,(0,0))
        pygame.draw.rect(screen,'Pink',textRect,0,5)
        pygame.draw.rect(screen,'Red',textRect,5)

        screen.blit(textSurf,textRect)
        displayScore()
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
            gameActive=False
            snail_rect.x=800

    else:
        screen.fill('Yellow')
        screen.blit(text_playAgain_surface,text_PlayAgain_rect)
 
    pygame.display.update()
    clock.tick(30)
