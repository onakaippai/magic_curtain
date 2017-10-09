import pygame
import time

pygame.init()
pygame.display.set_caption('Magic Curtain')
clock = pygame.time.Clock()

height_screen = 700
width_screen = 600
screen = pygame.display.set_mode((width_screen,height_screen))

black       = (0,   0,   0)
white       = (255, 255, 255)
gray        = (180, 180, 180)
light_gray  = (220, 220, 220)
red         = (255, 50,  50 )
light_red   = (255, 90,  90 )
red         = (50,  255, 50 )
light_red   = (90,  255, 90 )

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def exit_message():    
    exit_btn = True    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    exit_btn = True 
                if event.key == pygame.K_RIGHT:
                    exit_btn = False 
                if event.key == pygame.K_RETURN:
                    if exit_btn:
                        pygame.quit()
                        quit()  
                    else:
                        return
                
        screen.fill((white))  
        pygame.draw.rect(screen, black, [50, 150, 500, 300])
        pygame.draw.rect(screen, white, [60, 160, 480, 280])
        textFont = pygame.font.Font('freesansbold.ttf',35)
        textSurf, textRect = text_objects('Finish Aapplication?',textFont)
        textRect.center = (300,200)
        screen.blit(textSurf,textRect)         
        
        if exit_btn:
            pygame.draw.rect(screen, gray, [120, 330, 80, 60])            
        else:
            pygame.draw.rect(screen, gray, [400, 330, 80, 60])
        pygame.draw.rect(screen, light_gray, [122, 332, 76, 56])
        pygame.draw.rect(screen, light_gray, [402, 332, 76, 56])
            
        textFont = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects('Yes',textFont)
        textRect.center = (160,360)
        screen.blit(textSurf,textRect) 

        textFont = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects('No',textFont)
        textRect.center = (440,360)
        screen.blit(textSurf,textRect)  
                
        pygame.display.update()
        clock.tick(60)
        
        

def prepare_images():
    pass

def create_texture():
    pass

def get_score():
    pass

def main_menu():
    pass

def generation_start(idx_step):
    pass

def generation_end(idx_step):
    pass

def clac_params(idx_step):
    pass
    
def show_and_score(idx_step):
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_message()
    
    screen.fill((white))   
    pygame.display.update()
    clock.tick(60)