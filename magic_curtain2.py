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
img_heart = pygame.transform.scale(pygame.image.load(imgpath + 'heart2.png'),(50,50))
mask_wall = pygame.transform.scale(pygame.image.load(imgpath + 'wall_mask.png'),(height_screen,height_screen))
mask_window = pygame.transform.scale(pygame.image.load(imgpath + 'window_mask.png'),(height_screen,height_screen))
mask_curtain = pygame.transform.scale(pygame.image.load(imgpath + 'curtain_mask2.png'),(height_screen,height_screen))

season_or_wall = True
curtain_param = zeros((30,33))
line_param = []
fore_param = []
curtain_score = [] 
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
        now = pygame.time.get_ticks()
        screen.fill(white)
        wel_surf = pygame.Surface((width_screen, height_screen))
        wel_surf.fill((0,0,0), special_flags=pygame.BLEND_RGBA_SUB)        
        
        textSurf, textRect = text_objects('Welcome to','comicsansms',100, black)
        textRect.center = (500,200)
        wel_surf.blit(textSurf,textRect)  
        
        textSurf, textRect = text_objects('Magic Curtain','comicsansms',100, black)
        textRect.center = (500,400)
        wel_surf.blit(textSurf,textRect) 
        
        wel_surf.set_colorkey((0,0,0))
#        wel_surf.set_alpha(255)
        if (now - start) < 1250: 
            wel_surf.set_alpha((now - start)/5)  
        if (now - start) > 3750: 
            wel_surf.set_alpha(255-(now - start - 3750)/5)   
        screen.blit(wel_surf,(0,0))
        pygame.display.update() 
        
        if (now - start) > 5000:          
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
    global fore_param
    
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
    
    line_surf = pygame.Surface((img_outside.get_width()/2, img_outside.get_height()))
    line_surf.fill((0,0,0))
    
    if curtain_param[idx_curtain][19]<50:
        pass
    else:
        if curtain_param[idx_curtain][16]<50:
            x_step = 300 / curtain_param[idx_curtain][17]
            y_step = 600 / curtain_param[idx_curtain][18]
            rect_color = (min(255,max(0,curtain_param[idx_curtain][1] + curtain_param[idx_curtain][9])), \
                          min(255,max(0,curtain_param[idx_curtain][2] + curtain_param[idx_curtain][9])), \
                          min(255,max(0,curtain_param[idx_curtain][3] + curtain_param[idx_curtain][9])))
            for i  in range(int(curtain_param[idx_curtain][17])):
                for j  in range(int(curtain_param[idx_curtain][18])):
                    if i % 2:
                        pygame.draw.rect(line_surf, rect_color, [x_step*i, y_step*j, x_step, y_step/2])
                    else:
                        pygame.draw.rect(line_surf, rect_color, [x_step*i, y_step*j+y_step/2, x_step, y_step/2])
        else:
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
                    line_param[i][5] = randint(line_step*curtain_param[idx_curtain][5]/100,line_step*curtain_param[idx_curtain][6]/100)     
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
                        pygame.draw.line(line_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), start_pos, end_pos, line_param[i][5])
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
                                    points.append( (line_start + line_step*i +line_param[i][5]/2, tmp))
                                else:
                                    points.append( (line_start + line_step*(i+1) -line_param[i][5]/2, tmp) )                    
                        else:
                            tmp = start_pos[0]
                            for j in range(line_param[i][6]):                        
                                if curtain_param[idx_curtain][10] < 50: 
                                    tmp = start_pos[0] + (end_pos[0] - start_pos[0]) * 2**(j-line_param[i][6])
                                else:
                                    tmp = tmp + (end_pos[0] - start_pos[0]) * 2**(-j-1)
                                if j % 2:
                                    points.append( (tmp,line_start + line_step*i +line_param[i][5]/2))
                                else:
                                    points.append( (tmp,line_start + line_step*(i+1) -line_param[i][5]/2) )  
                        points.append( end_pos )            
                        pygame.draw.lines(line_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), False, points, line_param[i][5])   
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
                        pygame.draw.line(line_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), start_pos, end_pos, line_param[i][5])
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
                                    points.append( (line_start + line_step*i +line_param[i][5]/2, tmp))
                                else:
                                    points.append( (line_start + line_step*(i+1) -line_param[i][5]/2, tmp) )                    
                        else:
                            tmp = start_pos[0]
                            for j in range(line_param[i][6]):                        
                                if curtain_param[idx_curtain][10] < 50: 
                                    tmp = start_pos[0] + (end_pos[0] - start_pos[0]) * 2**(j-line_param[i][6])
                                else:
                                    tmp = tmp + (end_pos[0] - start_pos[0]) * 2**(-j-1)
                                if j % 2:
                                    points.append( (tmp,line_start + line_step*i + line_param[i][5]/2))
                                else:
                                    points.append( (tmp,line_start + line_step*(i+1) - line_param[i][5]/2) )   
                        points.append( end_pos )            
                        pygame.draw.lines(line_surf, (line_param[i][0],line_param[i][1],line_param[i][2]), False, points, line_param[i][5])   
                     
        line_surf.set_colorkey((0,0,0))
        line_surf.set_alpha(255) 
        curtain_surf.blit(line_surf, (0, 0))
        curtain_surf.blit(pygame.transform.flip(line_surf,True,False), (300, 0))
        
        
    fore_surf = pygame.Surface((img_outside.get_width()/2, img_outside.get_height()))
    fore_surf.fill((0,0,0))
    if curtain_param[idx_curtain][20] < 50:
        pass
    else:
        if fore_param == []:
            fore_param = zeros((curtain_param[idx_curtain][21], 20))
            for i in range(int(curtain_param[idx_curtain][21])):
                fore_param[i][0] = randint(101)
                fore_color = []
                fore_color.append(randint(-curtain_param[idx_curtain][23],curtain_param[idx_curtain][23]))
                fore_color.append(randint(-curtain_param[idx_curtain][24],curtain_param[idx_curtain][24]))
                fore_color.append(randint(-curtain_param[idx_curtain][25],curtain_param[idx_curtain][25]))                
                fore_param[i][1] = min(255,max(0,curtain_param[idx_curtain][1] + fore_color[0]))
                fore_param[i][2] = min(255,max(0,curtain_param[idx_curtain][2] + fore_color[1]))
                fore_param[i][3] = min(255,max(0,curtain_param[idx_curtain][3] + fore_color[2]))
                if (fore_param[i][1],fore_param[i][2],fore_param[i][3]) == (0,0,0):
                    (fore_param[i][1],fore_param[i][2],fore_param[i][3]) = (1,1,1)
                fore_param[i][4] = 300 * randint(curtain_param[idx_curtain][26])/100
                fore_param[i][5] = 300 * randint(curtain_param[idx_curtain][27],300)/100
                fore_param[i][6] = 600 * randint(curtain_param[idx_curtain][28])/100
                fore_param[i][7] = 600 * randint(curtain_param[idx_curtain][29],300)/100
                fore_param[i][8] = randint(curtain_param[idx_curtain][30]*0.5, curtain_param[idx_curtain][30]*1.5 )
                fore_param[i][9] = randint(curtain_param[idx_curtain][31]*0.5, curtain_param[idx_curtain][31]*1.5 )
                fore_param[i][10] = randint(curtain_param[idx_curtain][32]*0.5, curtain_param[idx_curtain][32]*1.5 )
                fore_w = fore_param[i][5]-fore_param[i][4]
                fore_h = fore_param[i][7]-fore_param[i][6]
                if fore_param[i][0] < curtain_param[idx_curtain][22]: # ellipse
                    for j in range(int(fore_param[i][8])):
                        for k in range(int(fore_param[i][9])):
                            pygame.draw.ellipse(fore_surf,(fore_param[i][1],fore_param[i][2],fore_param[i][3]), \
                                                [fore_param[i][4] + j * fore_w /fore_param[i][8], \
                                                 fore_param[i][6] + k * fore_h /fore_param[i][9], \
                                                 fore_w * fore_param[i][10] / 100, \
                                                 fore_h * fore_param[i][10] / 200 ])
                else:
                    for j in range(int(fore_param[i][8])):
                        for k in range(int(fore_param[i][9])):
                            base_pose = (fore_param[i][4] + j * fore_w /fore_param[i][8],fore_param[i][6] + k * fore_h /fore_param[i][9]);
                            pygame.draw.polygon(fore_surf,(fore_param[i][1],fore_param[i][2],fore_param[i][3]), \
                                                [(base_pose[0]+fore_w * fore_param[i][10] / 100,base_pose[1]+fore_h * fore_param[i][10] / 200),\
                                                 (base_pose[0]+fore_w * fore_param[i][10] / 200,base_pose[1]),\
                                                 (base_pose[0],base_pose[1]+fore_h * fore_param[i][10] / 400)])
        else:
            for i in range(int(curtain_param[idx_curtain][21])):
                fore_w = fore_param[i][5]-fore_param[i][4]
                fore_h = fore_param[i][7]-fore_param[i][6]
                if fore_param[i][0] < curtain_param[idx_curtain][22]: # ellipse
                    for j in range(int(fore_param[i][8])):
                        for k in range(int(fore_param[i][9])):
                            pygame.draw.ellipse(fore_surf,(fore_param[i][1],fore_param[i][2],fore_param[i][3]), \
                                                [fore_param[i][4] + j * fore_w /fore_param[i][8], \
                                                 fore_param[i][6] + k * fore_h /fore_param[i][9], \
                                                 fore_w * fore_param[i][10] / 100, \
                                                 fore_h * fore_param[i][10] / 200 ])
                else:
                    for j in range(int(fore_param[i][8])):
                        for k in range(int(fore_param[i][9])):
                            base_pose = (fore_param[i][4] + j * fore_w /fore_param[i][8],fore_param[i][6] + k * fore_h /fore_param[i][9]);
                            pygame.draw.polygon(fore_surf,(fore_param[i][1],fore_param[i][2],fore_param[i][3]), \
                                                [(base_pose[0]+fore_w * fore_param[i][10] / 100,base_pose[1]+fore_h * fore_param[i][10] / 200),\
                                                 (base_pose[0]+fore_w * fore_param[i][10] / 200,base_pose[1]),\
                                                 (base_pose[0],base_pose[1]+fore_h * fore_param[i][10] / 400)])
        fore_surf.set_colorkey((0,0,0))
        fore_surf.set_alpha(255) 
        curtain_surf.blit(fore_surf, (0, 0))
        curtain_surf.blit(pygame.transform.flip(fore_surf,True,False), (300, 0))
    
    curtain_surf.blit(mask_curtain, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
    curtain_surf.set_colorkey((0,0,0))
    curtain_surf.set_alpha(curtain_param[idx_curtain][0]) 
    screen.blit(curtain_surf, (0,0))
    
def get_score(idx_curtain,curtain_score, click_flag):
    global line_param
    global fore_param
#    global idx_curtain
#    for event in pygame.event.get(): 
#        pass
        #print(pygame.mouse.get_pos())
    (mouse_x, mouse_y) = pygame.mouse.get_pos()    
    surf_score = pygame.Surface((400, 600))
    surf_score.fill(white)
    pygame.draw.line(surf_score,black,(150,150),(150,550),10)
    pygame.draw.line(surf_score,black,(130,145),(170,145),10)
    pygame.draw.line(surf_score,black,(130,555),(170,555),10)
    
    no_str = 'please score No.'+str(idx_curtain+1)+' curtain'
    textSurf, textRect = text_objects(no_str,'comicsansms',25, black)
    textRect.center = (200,30)
    surf_score.blit(textSurf,textRect)
    
    if idx_step == 2:
        num_total = 30
    else:
        num_total = 10
    textSurf, textRect = text_objects('by clicking on the rule' + '(of ' +str(num_total) +')','comicsansms',25, black)
    textRect.center = (200,80)
    surf_score.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('100','comicsansms',50, black)
    textRect.center = (70,145)
    surf_score.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('   0','comicsansms',50, black)
    textRect.center = (75,555)
    surf_score.blit(textSurf,textRect)
    
    for i in range(4):
        pygame.draw.line(surf_score,black,(140,230+80*i),(160,230+80*i),2)
        textSurf, textRect = text_objects(str(100-(i+1)*20),'comicsansms',20, black)
        textRect.center = (95,230+80*i)
        surf_score.blit(textSurf,textRect)
        
    if 730<mouse_x<770 and 149<mouse_y<551:
        surf_score.blit(img_heart,(125,mouse_y-25))          
        textSurf, textRect = text_objects(str(100 - (mouse_y-150)/4),'comicsansms',70, black)
        textRect.center = (290,mouse_y)
        surf_score.blit(textSurf,textRect)
        if pygame.mouse.get_pressed()[0]:
            if click_flag:
                click_flag = 0
            else:
                click_flag = 1
                line_param = []
                fore_param = []
                curtain_score.append(100 - (mouse_y-150)/4)
    #            print(curtain_score)
                return (idx_curtain + 1,curtain_score,click_flag)
    
            
#    surf_score.set_colorkey((0,0,0))
#    surf_score.set_alpha(255)    
    screen.blit(surf_score,(600,0))
    return (idx_curtain,curtain_score,click_flag)


def generation_start():
    start = pygame.time.get_ticks()
    while True: 
        for event in pygame.event.get():
            pass
        screen.fill(white)
        if idx_step == 7:
            textSurf, textRect = text_objects('getting result','comicsansms',100, black)
            textRect.center = (500,300)
            screen.blit(textSurf,textRect)            
        else:                
            textSurf, textRect = text_objects('preparing','comicsansms',100, black)
            textRect.center = (500,200)
            screen.blit(textSurf,textRect)
            if idx_step == 2:
                textSurf, textRect = text_objects('1st generation ...','comicsansms',100, black)
            elif idx_step == 3:
                textSurf, textRect = text_objects('2nd generation ...','comicsansms',100, black)
            elif idx_step == 4:
                textSurf, textRect = text_objects('3rd generation ...','comicsansms',100, black)
            elif idx_step == 5:
                textSurf, textRect = text_objects('4th generation ...','comicsansms',100, black)
            elif idx_step == 6:
                textSurf, textRect = text_objects('5th generation ...','comicsansms',100, black)
            textRect.center = (500,400)
            screen.blit(textSurf,textRect)  
        
        pygame.display.update() 
        now = pygame.time.get_ticks()
        if (now - start) > 2000:          
            break   

def generation_end():
    start = pygame.time.get_ticks()
    while True: 
        for event in pygame.event.get():
            pass
        screen.fill(white)
        textSurf, textRect = text_objects('calculating the results','comicsansms',60, black)
        textRect.center = (500,200)
        screen.blit(textSurf,textRect)
        if idx_step == 2:
            textSurf, textRect = text_objects('of 1st generation ...','comicsansms',60, black)
        elif idx_step == 3:
            textSurf, textRect = text_objects('of 2nd generation ...','comicsansms',60, black)
        elif idx_step == 4:
            textSurf, textRect = text_objects('of 3rd generation ...','comicsansms',60, black)
        elif idx_step == 5:
            textSurf, textRect = text_objects('of 4th generation ...','comicsansms',60, black)
        elif idx_step == 6:
            textSurf, textRect = text_objects('of 5th generation ...','comicsansms',60, black)
        textRect.center = (500,400)
        screen.blit(textSurf,textRect)  
        
        pygame.display.update() 
        now = pygame.time.get_ticks()
        if (now - start) > 2000:          
            break      
            
def clac_params(curtain_score):
    seed(pygame.time.get_ticks())
    global curtain_param
    # whole curtain
    #
    # line(Surface, color, start_pos, end_pos, width=1)
    # aalines(Surface, color, closed, pointlist, blend=1)
    if idx_step == 2:          
        for i in range(30):
            curtain_param[i][0] = randint(180) # surf alpha
            curtain_param[i][1] = randint(256) # background R
            curtain_param[i][2] = randint(256) # background G
            curtain_param[i][3] = randint(256) # background B
            
            curtain_param[i][4] = randint(1,30) # v line num
            curtain_param[i][5] = randint(1,50) # line width min %
            curtain_param[i][6] = randint(51,101) # line width max %
            curtain_param[i][7] = randint(1,50) # line long min %
            curtain_param[i][8] = randint(51,101) # line long max %
            curtain_param[i][9] = randint(1,200) # background R adjust range
            curtain_param[i][10] = randint(101) # line start %
            curtain_param[i][11] = randint(101) # line range start %
            curtain_param[i][12] = randint(101) # line band %
            curtain_param[i][13] = randint(101) # direction %
            
            curtain_param[i][14] = randint(101) # line or lines %
            curtain_param[i][15] = randint(5,30) # num of points (lines only)%
            
            curtain_param[i][16] = randint(101) # line or rect %             
            curtain_param[i][17] = randint(1,20) #  rect num h %  
            curtain_param[i][18] = randint(1,20) #  rect num v %            
            curtain_param[i][19] = randint(101) # no or have background %   
            
            # pygame.draw.ellipse(DISPLAYSURF, RED, (300, 200, 40, 80), 1)
            # polygon(Surface, color, pointlist, width=0)
            curtain_param[i][20] = randint(101) # no or have foreground
            curtain_param[i][21] = randint(1,20) # kinds of foreground
            curtain_param[i][22] = randint(101) # rate being ellipse %
            curtain_param[i][23] = randint(1,200) # foreground R adjust range
            curtain_param[i][24] = randint(1,200) # foreground G adjust range
            curtain_param[i][25] = randint(1,200) # foreground B adjust range
            curtain_param[i][26] = randint(1,50) # start foreground x %
            curtain_param[i][27] = randint(51,101) # end foreground x %
            curtain_param[i][28] = randint(1,50) # start foreground y %
            curtain_param[i][29] = randint(51,101) # end foreground y %
            curtain_param[i][30] = randint(1,15) #  num h %  
            curtain_param[i][31] = randint(1,30) #  num v %  
            curtain_param[i][32] = randint(1,30) #  size %
    else:
        curtain_rank = sorted(curtain_score,reverse=True)
        parents = zeros((3,33))
        parents[0] = curtain_param[curtain_score.index(curtain_rank[0])]
        parents[1] = curtain_param[curtain_score.index(curtain_rank[1])]
        parents[2] = curtain_param[curtain_score.index(curtain_rank[2])]
        
        cross_rate = 0.6
        mutate_rate = 0.15
        curtain_param = zeros((10,33))
        
        num_rand = rand(10,33)
        num_cross = num_rand < cross_rate
        num_nocross = ~num_cross
        
        num_rand = rand(10,33)
        num_mutate = num_rand < mutate_rate
        num_nomutate = ~num_mutate 
        
        for i in range(10):
            if i < 3:
                curtain_param[i] = parents[i]
            else:
                curtain_param[i] = (parents[0]*0.5 + parents[1]*0.5)*num_cross[i] + parents[0] * num_nocross[i]            
                curtain_param[i][0] = randint(180)*num_mutate[i][0] + curtain_param[i][0]*num_nomutate[i][0] # surf alpha
                curtain_param[i][1] = randint(256)*num_mutate[i][1] + curtain_param[i][1]*num_nomutate[i][1] # background R
                curtain_param[i][2] = randint(256)*num_mutate[i][2] + curtain_param[i][2]*num_nomutate[i][2] # background G
                curtain_param[i][3] = randint(256)*num_mutate[i][3] + curtain_param[i][3]*num_nomutate[i][3] # background B
                
                curtain_param[i][4] = randint(1,30)*num_mutate[i][4] + curtain_param[i][4]*num_nomutate[i][4] # v line num
                curtain_param[i][5] = randint(1,50)*num_mutate[i][5] + curtain_param[i][5]*num_nomutate[i][5] # line width min %
                curtain_param[i][6] = randint(51,101)*num_mutate[i][6] + curtain_param[i][6]*num_nomutate[i][6] # line width max %
                curtain_param[i][7] = randint(1,50)*num_mutate[i][7] + curtain_param[i][7]*num_nomutate[i][7] # line long min %
                curtain_param[i][8] = randint(51,101)*num_mutate[i][8] + curtain_param[i][8]*num_nomutate[i][8] # line long max %
                curtain_param[i][9] = randint(1,200)*num_mutate[i][9] + curtain_param[i][9]*num_nomutate[i][9] # background R adjust range
                curtain_param[i][10] = randint(101)*num_mutate[i][10] + curtain_param[i][10]*num_nomutate[i][10] # line start %
                curtain_param[i][11] = randint(101)*num_mutate[i][11] + curtain_param[i][11]*num_nomutate[i][11] # line range start %
                curtain_param[i][12] = randint(101)*num_mutate[i][12] + curtain_param[i][12]*num_nomutate[i][12] # line band %
                curtain_param[i][13] = randint(101)*num_mutate[i][13] + curtain_param[i][13]*num_nomutate[i][13] # direction %
                
                curtain_param[i][14] = randint(101)*num_mutate[i][14] + curtain_param[i][14]*num_nomutate[i][14] # line or lines %
                curtain_param[i][15] = randint(5,30)*num_mutate[i][15] + curtain_param[i][15]*num_nomutate[i][15] # num of points (lines only)%
                
                curtain_param[i][16] = randint(101)*num_mutate[i][16] + curtain_param[i][16]*num_nomutate[i][16] # line or rect %             
                curtain_param[i][17] = randint(1,20)*num_mutate[i][17] + curtain_param[i][17]*num_nomutate[i][17] #  rect num h %  
                curtain_param[i][18] = randint(1,20)*num_mutate[i][18] + curtain_param[i][18]*num_nomutate[i][18] #  rect num v %            
                curtain_param[i][19] = randint(101)*num_mutate[i][19] + curtain_param[i][19]*num_nomutate[i][19] # no or have background %   
                
                # pygame.draw.ellipse(DISPLAYSURF, RED, (300, 200, 40, 80), 1)
                # polygon(Surface, color, pointlist, width=0)
                curtain_param[i][20] = randint(101)*num_mutate[i][20] + curtain_param[i][20]*num_nomutate[i][20] # no or have foreground
                curtain_param[i][21] = randint(1,20)*num_mutate[i][21] + curtain_param[i][21]*num_nomutate[i][21] # kinds of foreground
                curtain_param[i][22] = randint(101)*num_mutate[i][22] + curtain_param[i][22]*num_nomutate[i][22] # rate being ellipse %
                curtain_param[i][23] = randint(1,200)*num_mutate[i][23] + curtain_param[i][23]*num_nomutate[i][23] # foreground R adjust range
                curtain_param[i][24] = randint(1,200)*num_mutate[i][24] + curtain_param[i][24]*num_nomutate[i][24] # foreground G adjust range
                curtain_param[i][25] = randint(1,200)*num_mutate[i][25] + curtain_param[i][25]*num_nomutate[i][25] # foreground B adjust range
                curtain_param[i][26] = randint(1,50)*num_mutate[i][26] + curtain_param[i][26]*num_nomutate[i][26] # start foreground x %
                curtain_param[i][27] = randint(51,101)*num_mutate[i][27] + curtain_param[i][27]*num_nomutate[i][27] # end foreground x %
                curtain_param[i][28] = randint(1,50)*num_mutate[i][28] + curtain_param[i][28]*num_nomutate[i][28] # start foreground y %
                curtain_param[i][29] = randint(51,101)*num_mutate[i][29] + curtain_param[i][29]*num_nomutate[i][29] # end foreground y %
                curtain_param[i][30] = randint(1,15)*num_mutate[i][30] + curtain_param[i][30]*num_nomutate[i][30] #  num h %  
                curtain_param[i][31] = randint(1,30)*num_mutate[i][31] + curtain_param[i][31]*num_nomutate[i][31] #  num v %  
                curtain_param[i][32] = randint(1,30)*num_mutate[i][32] + curtain_param[i][32]*num_nomutate[i][32] #  size %
            
            
        
    
def show_and_score(curtain_score):  
    idx_curtain = 0    
    generation_start()
    clac_params(curtain_score)
    curtain_score = []
    click_flag = 0
    while True:
        for event in pygame.event.get(): 
            #print(pygame.mouse.get_pos())                     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_box()
#                if event.key == pygame.K_RETURN:
#                    line_param = []
#                    fore_param = []
#                    idx_curtain += 1
        draw_curtain(idx_curtain)
        (idx_curtain, curtain_score,click_flag) = get_score(idx_curtain,curtain_score, click_flag)        
        pygame.display.update()
        if idx_curtain == 30 and idx_step == 2:            
            break       
        elif idx_curtain == 10 and idx_step > 2:
            break
    generation_end()
    return curtain_score


def show_res(curtain_score):    
    global curtain_param
    global line_param
    global fore_param
    generation_start()
    curtain_rank = sorted(curtain_score,reverse=True)
    res = zeros((2,33))
    res[0] = curtain_param[curtain_score.index(curtain_rank[0])]
    res[1] = curtain_param[curtain_score.index(curtain_rank[1])]
    curtain_param = res
    save_flag = 1
    line_param = []
    fore_param = []
    while True:
        for event in pygame.event.get(): 
            #print(pygame.mouse.get_pos())                     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_box()
        draw_curtain(0)
        textSurf, textRect = text_objects('I guess you like this.','comicsansms',30, black)
        textRect.center = (800,200)
        screen.blit(textSurf,textRect)
        textSurf, textRect = text_objects('And the curtain image','comicsansms',30, black)
        textRect.center = (800,300)
        screen.blit(textSurf,textRect)
        textSurf, textRect = text_objects(' has been saved.','comicsansms',30, black)
        textRect.center = (800,400)
        screen.blit(textSurf,textRect)
        pygame.display.update()    
        if save_flag:
            pygame.image.save(screen,'res.png')
            save_flag = 0
            
    
    

while True:
    if idx_step == 0:
        welcome()
        idx_step = 1
    elif idx_step == 1:
        main_menu()
        idx_step = 2
    elif idx_step == 7:
        # 5 generation
        show_res(curtain_score)
    else:
        curtain_score = show_and_score(curtain_score)
        idx_step += 1 
    #pygame.display.update()