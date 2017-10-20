import pygame
from numpy import *
from numpy.random import *

pygame.init()
pygame.display.set_caption('Magic Curtain')

height_screen = 600
width_screen = 1000
screen = pygame.display.set_mode((width_screen,height_screen))

black       = (1,   1,   1  )
white       = (255, 255, 255)
gray        = (180, 180, 180)
light_gray  = (220, 220, 220)
red         = (255, 50,  50 )
green       = (50,  255, 50 )
light_green = (150, 255, 150)
blue        = (50,  50,  255)
pink        = (255, 100, 180)
orange      = (255, 180, 100)

imgpath = 'D:/source/magic_curtain/img_pattern/'
img_spring = pygame.transform.scale(pygame.image.load(imgpath + 'spring.png'),(height_screen,height_screen))
img_summer = pygame.transform.scale(pygame.image.load(imgpath + 'summer.png'),(height_screen,height_screen))
img_autumn = pygame.transform.scale(pygame.image.load(imgpath + 'autumn.png'),(height_screen,height_screen))
img_winter = pygame.transform.scale(pygame.image.load(imgpath + 'winter.png'),(height_screen,height_screen))
img_curtain = pygame.transform.scale(pygame.image.load(imgpath + 'curtain.jpg'),(height_screen,height_screen))
mask_wall = pygame.transform.scale(pygame.image.load(imgpath + 'wall_mask.png'),(height_screen,height_screen))
mask_window = pygame.transform.scale(pygame.image.load(imgpath + 'window_mask.png'),(height_screen,height_screen))
mask_curtain = pygame.transform.scale(pygame.image.load(imgpath + 'curtain_mask2.png'),(height_screen,height_screen))

season_or_wall = True
curtain_param = zeros((100,100))
line_param = []
idx_season = 0
idx_wall = 0
idx_step = 0

def text_objects(text, font_type, font_size, color):
    textFont = pygame.font.SysFont(font_type,font_size)
    textSurface = textFont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def welcome():  
    start = pygame.time.get_ticks()
    while True: 
        for event in pygame.event.get():
            pass
        wel_surf = pygame.Surface((width_screen, height_screen))
        wel_surf.fill(white)
        
        textSurf, textRect = text_objects('Welcome to','comicsansms',100, black)
        textRect.center = (500,200)
        wel_surf.blit(textSurf,textRect)  
        
        textSurf, textRect = text_objects('Magic Curtain','comicsansms',100, black)
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
        textSurf, textRect = text_objects('Finish Application?','comicsansms',35, black)
        textRect.center = (250,100)
        exit_surf.blit(textSurf,textRect)           
        if exit_btn:
            pygame.draw.rect(exit_surf, gray, [50, 200, 80, 60])            
        else:
            pygame.draw.rect(exit_surf, gray, [370, 200, 80, 60])
        pygame.draw.rect(exit_surf, light_gray, [52, 202, 76, 56])
        pygame.draw.rect(exit_surf, light_gray, [372, 202, 76, 56])            
        textSurf, textRect = text_objects('Yes','comicsansms',20, black)
        textRect.center = (90,230)
        exit_surf.blit(textSurf,textRect) 
        textSurf, textRect = text_objects('No','comicsansms',20, black)
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
                if event.key == pygame.K_RETURN:
                    return
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
                    if idx_wall > 21:
                        idx_wall = 21                  
            
        screen.fill(white)        
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
        
        textSurf, textRect = text_objects('press enter to start','comicsansms',30, black)
        textRect.center = (800,25)
        screen.blit(textSurf,textRect) 
            
        if season_or_wall:
            textSurf, textRect = text_objects('*','comicsansms',100, gray)
            textRect.center = (720,100)
            screen.blit(textSurf,textRect) 
        else:
            textSurf, textRect = text_objects('*','comicsansms',100, gray)
            textRect.center = (900,100)
            screen.blit(textSurf,textRect) 
        if idx_season == 0:
            textSurf, textRect = text_objects('Spring','comicsansms',50, light_green)
        else:
            textSurf, textRect = text_objects('Spring','comicsansms',50, gray)
        textRect.center = (720,180)
        screen.blit(textSurf,textRect)
        if idx_season == 1:
            textSurf, textRect = text_objects('Summer','comicsansms',50, red)
        else:
            textSurf, textRect = text_objects('Summer','comicsansms',50, gray)
        textRect.center = (720,280)
        screen.blit(textSurf,textRect)
        if idx_season == 2:
            textSurf, textRect = text_objects('Autumn','comicsansms',50, orange)
        else:
            textSurf, textRect = text_objects('Autumn','comicsansms',50, gray)
        textRect.center = (720,380)
        screen.blit(textSurf,textRect)
        if idx_season == 3:
            textSurf, textRect = text_objects('Winter','comicsansms',50, blue)
        else:
            textSurf, textRect = text_objects('Winter','comicsansms',50, gray)
        textRect.center = (720,480)
        screen.blit(textSurf,textRect)
        
        pygame.draw.rect(screen, light_gray, [845, 115, 110, 450])
        textSurf, textRect = text_objects('>      <','monospace',30, black)
        textRect.center = (900,130+idx_wall*20)
        screen.blit(textSurf,textRect)
        for i in range(22):
            if i == 0:
                pygame.draw.rect(screen, white, [850, 120+i*20, 100, 20])
            elif i == 1:
                pygame.draw.rect(screen, light_gray, [850, 120+i*20, 100, 20])
            elif i == 2:
                pygame.draw.rect(screen, gray, [850, 120+i*20, 100, 20])
            elif i > 2:
                show_color = pygame.Color(0,0,0)
                show_color.hsva = ((i-3)*20,20,90,50)
                pygame.draw.rect(screen, show_color, [850, 120+i*20, 100, 20])
        pygame.display.update()

def draw_curtain(idx_curtain):
    global line_param
    
    if idx_season == 0:
        img_outside = img_spring
    elif idx_season == 1:
        img_outside = img_summer
    elif idx_season == 2:
        img_outside = img_autumn
    elif idx_season == 3:
        img_outside = img_winter
    
    screen.fill(white)
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
    
    curtain_surf = pygame.Surface((img_outside.get_width(), img_outside.get_height()))
    curtain_color = (curtain_param[idx_curtain][1], curtain_param[idx_curtain][2], curtain_param[idx_curtain][3])
    curtain_surf.fill(curtain_color)
    
    if curtain_param[idx_curtain][13]<50:
        line_size = 300 # v
        num_line = int(curtain_param[idx_curtain][4])
    else:
        line_size = 600 # h
        num_line = int(curtain_param[idx_curtain][4]) * 2
    if curtain_param[idx_curtain][11] < 50:
        line_start = 0
        line_end = line_size * curtain_param[idx_curtain][12]/100
    else:
        line_start = line_size - line_size * curtain_param[idx_curtain][12]/100
        line_end = line_size                                                  
    line_range = line_end - line_start + 1                        
    
    line_step = line_range/curtain_param[idx_curtain][4]
    if line_param == []:
        line_param = zeros((num_line, 7), dtype = int)        
        for i in range(num_line):
            line_color = randint(-curtain_param[idx_curtain][9],curtain_param[idx_curtain][9])
            line_param[i][0] = min(255,max(0,curtain_param[idx_curtain][1] + line_color))
            line_param[i][1] = min(255,max(0,curtain_param[idx_curtain][2] + line_color))
            line_param[i][2] = min(255,max(0,curtain_param[idx_curtain][3] + line_color))
            if (line_param[i][0],line_param[i][1],line_param[i][2]) == (0,0,0):
                (line_param[i][0],line_param[i][1],line_param[i][2]) = (1,1,1)
            line_param[i][3] = randint(line_start + line_step*i, line_start + line_step*(i+1))
            line_param[i][4] = randint(curtain_param[idx_curtain][7], curtain_param[idx_curtain][8])
            if curtain_param[idx_curtain][13] < 50:        
                if curtain_param[idx_curtain][10] < 50:            
                    start_pos = (line_param[i][3],0)
                    end_pos = (line_param[i][3],600 * line_param[i][4]/100)
                else:
                    start_pos = (line_param[i][3],600- 600 *line_param[i][4]/100)
                    end_pos = (line_param[i][3],600)
            else:
                if curtain_param[idx_curtain][10] < 50:            
                    start_pos = (0,line_param[i][3])
                    end_pos = (300*line_param[i][4]/100,line_param[i][3])
                else:
                    start_pos = (300-300*line_param[i][4]/100,line_param[i][3])
                    end_pos = (300,line_param[i][3])
            line_param[i][5] = randint(line_step*curtain_param[idx_curtain][5]/100,line_step*curtain_param[idx_curtain][6]/100)            
            if curtain_param[idx_curtain][14] < 50:
                pygame.draw.line(curtain_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), start_pos, end_pos, line_param[i][5])
            else:
                line_param[i][6] = randint(1,curtain_param[idx_curtain][15])
                points = []
                points.append( start_pos )
                if curtain_param[idx_curtain][13] < 50: 
                    tmp = start_pos[1]                     
                    for j in range(line_param[i][6]):
                        if curtain_param[idx_curtain][10] < 50: 
                            tmp = start_pos[1] + (end_pos[1] - start_pos[1]) * 2**(j-line_param[i][6])
                        else:
                            tmp = tmp + (end_pos[1] - start_pos[1]) * 2**(-j-1)
                        if j % 2:
                            points.append( (line_start + line_step*i, tmp))
                        else:
                            points.append( (line_start + line_step*(i+1), tmp) )                    
                else:
                    for j in range(line_param[i][6]):
                        tmp = start_pos[0]
                        if curtain_param[idx_curtain][10] < 50: 
                            tmp = start_pos[0] + (end_pos[0] - start_pos[0]) * 2**(j-line_param[i][6])
                        else:
                            tmp = tmp + (end_pos[0] - start_pos[0]) * 2**(-j-1)
                        if j % 2:
                            points.append( (tmp,line_start + line_step*i))
                        else:
                            points.append( (tmp,line_start + line_step*(i+1)) )   
                points.append( end_pos )            
                pygame.draw.lines(curtain_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), False, points, line_param[i][5])   
    else:
        for i in range(num_line):
            if curtain_param[idx_curtain][13] < 50:        
                if curtain_param[idx_curtain][10] < 50:            
                    start_pos = (line_param[i][3],0)
                    end_pos = (line_param[i][3],600 * line_param[i][4]/100)
                else:
                    start_pos = (line_param[i][3],600- 600 *line_param[i][4]/100)
                    end_pos = (line_param[i][3],600)
            else:
                if curtain_param[idx_curtain][10] < 50:            
                    start_pos = (0,line_param[i][3])
                    end_pos = (300*line_param[i][4]/100,line_param[i][3])
                else:
                    start_pos = (300-300*line_param[i][4]/100,line_param[i][3])
                    end_pos = (300,line_param[i][3])
            if curtain_param[idx_curtain][14] < 50:
                pygame.draw.line(curtain_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), start_pos, end_pos, line_param[i][5])
            else:
                points = []
                points.append( start_pos )
                if curtain_param[idx_curtain][13] < 50: 
                    tmp = start_pos[1]                     
                    for j in range(line_param[i][6]):
                        if curtain_param[idx_curtain][10] < 50: 
                            tmp = start_pos[1] + (end_pos[1] - start_pos[1]) * 2**(j-line_param[i][6])
                        else:
                            tmp = tmp + (end_pos[1] - start_pos[1]) * 2**(-j-1)
                        if j % 2:
                            points.append( (line_start + line_step*i, tmp))
                        else:
                            points.append( (line_start + line_step*(i+1), tmp) )                    
                else:
                    for j in range(line_param[i][6]):
                        tmp = start_pos[0]
                        if curtain_param[idx_curtain][10] < 50: 
                            tmp = start_pos[0] + (end_pos[0] - start_pos[0]) * 2**(j-line_param[i][6])
                        else:
                            tmp = tmp + (end_pos[0] - start_pos[0]) * 2**(-j-1)
                        if j % 2:
                            points.append( (tmp,line_start + line_step*i))
                        else:
                            points.append( (tmp,line_start + line_step*(i+1)) )   
                points.append( end_pos )            
                pygame.draw.lines(curtain_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), False, points, line_param[i][5])   
            
    
    curtain_surf.blit(mask_curtain, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
    curtain_surf.set_colorkey((0,0,0))
    curtain_surf.set_alpha(curtain_param[idx_curtain][0]) 
    screen.blit(curtain_surf, (0,0))
    
def get_score():
    pass

def generation_start():
    start = pygame.time.get_ticks()
    while True: 
        for event in pygame.event.get():
            pass
        screen.fill(white)
        textSurf, textRect = text_objects('preparing','comicsansms',100, black)
        textRect.center = (500,200)
        screen.blit(textSurf,textRect)
        if idx_step == 2:
            textSurf, textRect = text_objects('1st generation ...','comicsansms',100, black)
        textRect.center = (500,400)
        screen.blit(textSurf,textRect)  
        
        pygame.display.update() 
        now = pygame.time.get_ticks()
        if (now - start) > 3000:          
            break   

def generation_end():
    pass

def clac_params():
    seed(idx_step)
    # whole curtain
    #
    # line(Surface, color, start_pos, end_pos, width=1)
    # aalines(Surface, color, closed, pointlist, blend=1)
    if idx_step == 2:          
        for i in range(100):
            curtain_param[i][0] = randint(180) # surf alpha
            curtain_param[i][1] = randint(255) # background R
            curtain_param[i][2] = randint(255) # background G
            curtain_param[i][3] = randint(255) # background B
            
            curtain_param[i][4] = randint(30) # v line num
            curtain_param[i][5] = randint(50) # line width min %
            curtain_param[i][6] = randint(51,101) # line width max %
            curtain_param[i][7] = randint(50) # line long min %
            curtain_param[i][8] = randint(51,101) # line long max %
            curtain_param[i][9] = randint(255) # line R adjust range
            curtain_param[i][10] = randint(101) # line start %
            curtain_param[i][11] = randint(101) # line range start %
            curtain_param[i][12] = randint(101) # line range %
            curtain_param[i][13] = randint(101) # direction %
            
            curtain_param[i][14] = randint(101) # line or aalines %
            curtain_param[i][15] = randint(3,20) # num of points %
            
            
        
    
def show_and_score():
    global line_param
    generation_start()
    clac_params()
    idx_curtain = 0
    while True:
        for event in pygame.event.get():                      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_box()
                if event.key == pygame.K_RETURN:
                    line_param = []
                    idx_curtain += 1
        draw_curtain(idx_curtain)
        get_score()        
        pygame.display.update()
    generation_end()

while True:
    if idx_step == 0:
        welcome()
        idx_step = 1
    elif idx_step == 1:
        main_menu()
        idx_step = 2
    elif idx_step == 7:
        # 5 generation
        break
    else:
        show_and_score()
        idx_step += 1 
    pygame.display.update()