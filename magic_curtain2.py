import pygame

pygame.init()
pygame.display.set_caption('Magic Curtain')

height_screen = 600
width_screen = 1000
screen = pygame.display.set_mode((width_screen,height_screen))

black       = (1,   1,   1,   255)
white       = (255, 255, 255, 255)
gray        = (180, 180, 180, 255)
light_gray  = (220, 220, 220, 255)
red         = (255, 50,  50,  255)
light_red   = (255, 90,  90,  255)
red         = (50,  255, 50,  255)
light_red   = (90,  255, 90,  255)
blue        = (50,  50,  255, 255)
light_blue  = (90,  90,  255, 255)

imgpath = 'D:/source/magic_curtain/img_pattern/'
img_spring = pygame.transform.scale(pygame.image.load(imgpath + 'spring.png'),(height_screen,height_screen))
img_summer = pygame.transform.scale(pygame.image.load(imgpath + 'summer.png'),(height_screen,height_screen))
img_autumn = pygame.transform.scale(pygame.image.load(imgpath + 'autumn.png'),(height_screen,height_screen))
img_winter = pygame.transform.scale(pygame.image.load(imgpath + 'winter.png'),(height_screen,height_screen))
img_curtain = pygame.transform.scale(pygame.image.load(imgpath + 'curtain.jpg'),(height_screen,height_screen))
mask_wall = pygame.transform.scale(pygame.image.load(imgpath + 'wall_mask.png'),(height_screen,height_screen))
mask_window = pygame.transform.scale(pygame.image.load(imgpath + 'window_mask.png'),(height_screen,height_screen))
mask_curtain = pygame.transform.scale(pygame.image.load(imgpath + 'curtain_mask.png'),(height_screen,height_screen))

season_or_wall = True
idx_season = 0
idx_wall = 0
idx_step = 0

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0,0))
    return textSurface, textSurface.get_rect()

def welcome():  
    start = pygame.time.get_ticks()
    while True: 
        for event in pygame.event.get():
            pass
        wel_surf = pygame.Surface((width_screen, height_screen))
        wel_surf.fill(white)
        
        textFont = pygame.font.Font('freesansbold.ttf',100)
        textSurf, textRect = text_objects('Welcome to',textFont)
        textRect.center = (500,200)
        wel_surf.blit(textSurf,textRect)  
        
        textFont = pygame.font.Font('freesansbold.ttf',100)
        textSurf, textRect = text_objects('Magic Curtain',textFont)
        textRect.center = (500,400)
        wel_surf.blit(textSurf,textRect) 
        
        screen.blit(wel_surf,(0,0))
        pygame.display.update() 
        now = pygame.time.get_ticks()
        if (now - start) > 3000:          
            break       
      

def exit_box():    
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
        height_exit_surf = 300
        width_exit_surf = 500
        exit_surf = pygame.Surface((width_exit_surf, height_exit_surf))
        exit_surf.fill(black)
        pygame.draw.rect(exit_surf, white, [10, 10, 480, 280])        
        textFont = pygame.font.Font('freesansbold.ttf',35)
        textSurf, textRect = text_objects('Finish Application?',textFont)
        textRect.center = (250,100)
        exit_surf.blit(textSurf,textRect)           
        if exit_btn:
            pygame.draw.rect(exit_surf, gray, [50, 200, 80, 60])            
        else:
            pygame.draw.rect(exit_surf, gray, [370, 200, 80, 60])
        pygame.draw.rect(exit_surf, light_gray, [52, 202, 76, 56])
        pygame.draw.rect(exit_surf, light_gray, [372, 202, 76, 56])            
        textFont = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects('Yes',textFont)
        textRect.center = (90,230)
        exit_surf.blit(textSurf,textRect) 
        textFont = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects('No',textFont)
        textRect.center = (410,230)
        exit_surf.blit(textSurf,textRect)        
        screen.blit(exit_surf, (250,100))
        pygame.display.update()  
        
def main_menu():
    global season_or_wall
    global idx_season
    global idx_wall  
    while True:
        for event in pygame.event.get():                      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    season_or_wall = True
                if event.key == pygame.K_RIGHT:
                    season_or_wall = False
                if event.key == pygame.K_ESCAPE:
                    exit_box()
                if season_or_wall:  
                    if event.key == pygame.K_UP:
                        idx_season -= 1
                    if event.key == pygame.K_DOWN:
                        idx_season += 1
                    if idx_season < 0:
                        idx_season = 0
                    if idx_season > 3:
                        idx_season = 3
                else:
                    if event.key == pygame.K_UP:
                        idx_wall -= 1
                    if event.key == pygame.K_DOWN:
                        idx_wall += 1   
                    if idx_wall < 0:
                        idx_wall = 0
                    if idx_wall > 20:
                        idx_wall = 20                  
            
        screen.fill(white)
        img_outside = img_spring
        if idx_season == 0:
            img_outside = img_spring
        elif idx_season == 1:
            img_outside = img_summer
        elif idx_season == 2:
            img_outside = img_autumn
        elif idx_season == 3:
            img_outside = img_winter
            
        screen.blit(img_curtain,(0,0))
        window_surf = pygame.Surface((img_outside.get_width(), img_outside.get_height())).convert()
        window_surf.blit(img_outside, (0, 0))
        window_surf.blit(mask_window, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
        window_surf.set_colorkey((0,0,0))
        window_surf.set_alpha(180) 
        screen.blit(window_surf, (0,0))
        
        wall_surf = pygame.Surface((img_outside.get_width(), img_outside.get_height()))  
        if idx_wall == 0:
            wall_color = white
        elif idx_wall == 1:
            wall_color = light_gray
        elif idx_wall == 2:
            wall_color = gray
        elif idx_wall > 2:
            wall_color = pygame.Color(0,0,0)
            wall_color.hsva = ((idx_wall-3)*20,10,90,100)
        wall_surf.fill(wall_color)
        wall_surf.blit(mask_wall, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
        wall_surf.set_colorkey((0,0,0))
        wall_surf.set_alpha(180) 
        screen.blit(wall_surf, (0,0))        
        
        pygame.display.update()

def prepare_images():
    pass

def create_texture():
    pass

def get_score():
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
    if idx_step == 0:
        welcome()
        idx_step = 1
    elif idx_step == 1:
        main_menu()
        idx_step = 2      
    pygame.display.update()