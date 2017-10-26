import os
import pygame
from numpy import *
from numpy.random import *

pygame.init()

class mc_class:
    
    
    def __init__(self):
        self.name         = 'Magic Curtain'        
        self.root_path    = os.path.abspath('..')      
        self.size_screen  = (1000, 600) # [width, height]
        self.size_curtain = (600, 600)  # [width, height]           
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((self.size_screen[0],self.size_screen[1]))        
        self.set_step_control()
        self.set_color()
        self.set_text_info()
        self.set_images()
      
    
    def set_step_control(self):
        self.idx_step       = 0           # program steps (welcome, main menu, genetic algorithm, save result)
        self.is_start       = True        # prepare new generation(True), or calculate generation result(False)
        self.flag_finish    = False       # finish genetic algorithm part, save the result (depends on generation number)
        self.time_welcome   = [1250, 3750, 5000]
        self.time_otherwise = 2000
        
        
    def set_color(self):
        self.color_key    = (0, 0, 0,)  # transparent color
        self.color = {}
        self.color['white']       = (255, 255, 255)
        self.color['light_gray']  = (220, 220, 220)
        self.color['gray']        = (180, 180, 180)
        self.color['black']       = (1,   1,   1  )
        self.color['red']         = (255, 50,  50 )
        self.color['light_green'] = (150, 255, 150)
        self.color['green']       = (50,  255, 50 )
        self.color['blue']        = (50,  50,  255)
        self.color['pink']        = (255, 100, 180)
        self.color['orange']      = (255, 180, 100)
        
        
    def set_text_info(self):
        self.text_welcome = ['Welcome to','Magic Curtain']
        self.text_start = ['preparing', ' generation ...']
        self.text_end = ['calculating the results', 'of ', ' generation ...']
        self.text_num = ['1st', '2nd', '3rd']
        for i in range(4,11):
            self.text_num.append(str(i)+'th')
        self.text_finish = 'getting result'
       
        
    def set_images(self):
        path_image        = os.path.join(self.root_path, 'img')        
        self.img_curtain  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'curtain.jpg')),(self.size_curtain[0], self.size_curtain[1]))
        self.img_heart    = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'heart.png')),(50, 50))
        self.mask_wall    = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'wall_mask.png')),(self.size_curtain[0], self.size_curtain[1]))
        self.mask_window  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'window_mask.png')),(self.size_curtain[0], self.size_curtain[1]))
        self.mask_curtain = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'curtain_mask.png')),(self.size_curtain[0], self.size_curtain[1]))
        
        
    def text_object(self, text, type_font, size_font, color_text):
        font_text = pygame.font.SysFont(type_font,size_font)
        surf_text = font_text.render(text, True, color_text)
        return surf_text, surf_text.get_rect()
        
    def show_message(self):
        # all message scene
        time_start = pygame.time.get_ticks()
        while True: 
            now_time = pygame.time.get_ticks()
            self.screen.fill(self.color['white']) 
            surf_screen = pygame.Surface((self.size_screen[0],self.size_screen[1]))
            surf_screen.fill(self.color_key, special_flags=pygame.BLEND_RGBA_SUB)             
            if self.idx_step == 0: # welcome 
                surf_text_upper, rect_text_upper = self.text_object(self.text_welcome[0],'comicsansms',120, self.color['black'])
                surf_text_lower, rect_text_lower = self.text_object(self.text_welcome[1],'comicsansms',120, self.color['black'])
            elif self.flag_finish:
                surf_text, rect_text = self.text_object(self.text_finish,'comicsansms',100, self.color['black'])
            else:         
                if self.is_start:
                    surf_text_upper, rect_text_upper = self.text_object(self.text_start[0],'comicsansms',80, self.color['black'])
                    surf_text_lower, rect_text_lower = self.text_object(self.text_num[self.idx_step-1]+self.text_start[1],'comicsansms',80, self.color['black'])
                else:
                    surf_text_upper, rect_text_upper = self.text_object(self.text_end[0],'comicsansms',80, self.color['black'])
                    surf_text_lower, rect_text_lower = self.text_object(self.text_end[1]+self.text_num[self.idx_step-1]+self.text_end[2],'comicsansms',80, self.color['black'])     
            if self.flag_finish:
                rect_text.center = (self.size_screen[0]* 1/2, self.size_screen[1] * 1/2)
                surf_screen.blit(surf_text, rect_text)      
            else:                
                rect_text_upper.center = (self.size_screen[0]* 1/2, self.size_screen[1] * 1/3)
                rect_text_lower.center = (self.size_screen[0]* 1/2, self.size_screen[1] * 2/3)
                surf_screen.blit(surf_text_upper, rect_text_upper)
                surf_screen.blit(surf_text_lower, rect_text_lower)    
            surf_screen.set_colorkey(self.color_key)            
            cnt_time = now_time - time_start
            # check show time
            if self.idx_step == 0:
                if cnt_time < self.time_welcome[0]:
                    surf_screen.set_alpha( cnt_time / 5 )
                if cnt_time > self.time_welcome[1]:
                    surf_screen.set_alpha( 255 - (cnt_time - self.time_welcome[1]) / 5 )
                if cnt_time > self.time_welcome[2]:
                    break
            else:
                if cnt_time > self.time_otherwise:
                    break
            self.screen.blit(surf_screen,(0,0))
            pygame.display.update()
    

    def exit_box(self):
        flag_exit = False    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        flag_exit = True 
                    if event.key == pygame.K_RIGHT:
                        flag_exit = False 
                    if event.key == pygame.K_RETURN:
                        if flag_exit:
                            pygame.quit()
                        else:
                            return       
            surf_exit = pygame.Surface((500, 300))
            surf_exit.fill(self.color['black'])
            pygame.draw.rect(surf_exit, self.color['white'], [10, 10, 480, 280])        
            surf_text, rect_text = self.text_object('Finish Application?','comicsansms',35, self.color['black'])
            rect_text.center = (250,100)
            surf_exit.blit(surf_text,rect_text)    
            # show focus point (yes or no) 
            if flag_exit:
                pygame.draw.rect(surf_exit, self.color['gray'], [50, 200, 80, 60])            
            else:
                pygame.draw.rect(surf_exit, self.color['gray'], [370, 200, 80, 60])
            pygame.draw.rect(surf_exit, self.color['light_gray'], [52, 202, 76, 56])
            pygame.draw.rect(surf_exit, self.color['light_gray'], [372, 202, 76, 56])            
            surf_text, rect_text = self.text_object('Yes','comicsansms',20, self.color['black'])
            rect_text.center = (90,230)
            surf_exit.blit(surf_text, rect_text) 
            surf_text, rect_text = self.text_object('No','comicsansms',20, self.color['black'])
            rect_text.center = (410,230)
            surf_exit.blit(surf_text,rect_text)        
            self.screen.blit(surf_exit, (250,100))
            pygame.display.update()  
    
    
    def load_season_images(self):
        path_image  = os.path.join(self.root_path, 'img')        
        img_spring  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'spring.jpg')),(self.size_curtain[0], self.size_curtain[1]))
        img_summer  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'summer.jpg')),(self.size_curtain[0], self.size_curtain[1]))
        img_autumn  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'autumn.jpg')),(self.size_curtain[0], self.size_curtain[1]))
        img_winter  = pygame.transform.scale(pygame.image.load(os.path.join(path_image, 'winter.jpg')),(self.size_curtain[0], self.size_curtain[1]))
        return [img_spring, img_summer, img_autumn, img_winter]

        
    def main_menu(self):        
        flag_season  = True # select outside season or wall color
        idx_season   = 0
        idx_wall     = 0
        num_season   = 4
        num_wall     = 22
        img_season   = self.load_season_images()
        text_season  = ['Spring', 'Summer', 'Autumn', 'Winter']  
        color_season = ['light_green', 'red', 'orange', 'blue']
        
        while True:
            for event in pygame.event.get():                      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit_box()
                    if event.key == pygame.K_LEFT:
                        flag_season = True
                    if event.key == pygame.K_RIGHT:
                        flag_season = False                    
                    if event.key == pygame.K_RETURN:
                        self.surf_window = surf_window
                        self.surf_wall   = surf_wall
                        return
                    if flag_season:  
                        if event.key == pygame.K_UP:
                            idx_season -= 1
                        if event.key == pygame.K_DOWN:
                            idx_season += 1
                        if idx_season < 0:
                            idx_season = 0
                        if idx_season > (num_season-1):
                            idx_season = num_season-1
                    else:
                        if event.key == pygame.K_UP:
                            idx_wall -= 1
                        if event.key == pygame.K_DOWN:
                            idx_wall += 1   
                        if idx_wall < 0:
                            idx_wall = 0
                        if idx_wall > (num_wall - 1):
                            idx_wall = num_wall - 1   
            self.screen.fill(self.color['white'])  
            self.screen.blit(self.img_curtain,(0,0))
            
            img_outside = img_season[idx_season]  
            surf_window = pygame.Surface((self.size_curtain[0], self.size_curtain[1]))
            surf_window.blit(img_outside,(0,0))
            surf_window.blit(self.mask_window, (0,0), special_flags=pygame.BLEND_RGBA_SUB)  
            surf_window.set_colorkey(self.color_key)
            surf_window.set_alpha(180) 
            self.screen.blit(surf_window, (0,0))
            
            surf_wall = pygame.Surface((self.size_curtain[0], self.size_curtain[1]))
            if idx_wall == 0:
                color_wall = self.color['white']
            elif idx_wall == 1:
                color_wall = self.color['light_gray']
            elif idx_wall == 2:
                color_wall = self.color['gray']
            elif idx_wall > 2:
                color_wall = pygame.Color(0,0,0)
                color_wall.hsva = ((idx_wall-3)*20,10,90,100)
            surf_wall.fill(color_wall)
            surf_wall.blit(self.mask_wall, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
            surf_wall.set_colorkey(self.color_key)
            surf_wall.set_alpha(180) 
            self.screen.blit(surf_wall, (0,0))
            
            # check focus point
            surf_text, rect_text = self.text_object('press enter to start','comicsansms',30, self.color['black'])
            rect_text.center = (800,25)
            self.screen.blit(surf_text, rect_text) 
            surf_text, rect_text = self.text_object('*','comicsansms',100, self.color['gray'])    
            if flag_season:                
                rect_text.center = (720,100)                
            else:                
                rect_text.center = (900,100)
            self.screen.blit(surf_text, rect_text) 
            
            # write season text
            for i in range(4):
                surf_text, rect_text = self.text_object(text_season[i],'comicsansms',50, self.color['gray'])
                rect_text.center = (720, 180 + 100 * i)
                self.screen.blit(surf_text, rect_text)                
            surf_text, rect_text = self.text_object(text_season[idx_season],'comicsansms',50, self.color[color_season[idx_season]])
            rect_text.center = (720, 180 + 100 * idx_season)
            self.screen.blit(surf_text, rect_text)
            
            # focus wall color
            pygame.draw.rect(self.screen, self.color['light_gray'], [845, 115, 110, 450])
            surf_text, rect_text = self.text_object('>      <','monospace',30, self.color['black'])
            rect_text.center = (900,130+idx_wall*20)
            self.screen.blit(surf_text, rect_text) 
            for i in range(22):
                if i == 0:
                    pygame.draw.rect(self.screen, self.color['white'], [850, 120+i*20, 100, 20])
                elif i == 1:
                    pygame.draw.rect(self.screen, self.color['light_gray'], [850, 120+i*20, 100, 20])
                elif i == 2:
                    pygame.draw.rect(self.screen, self.color['gray'], [850, 120+i*20, 100, 20])
                elif i > 2:
                    color_show = pygame.Color(0,0,0)
                    color_show.hsva = ((i-3)*20,20,90,50)
                    pygame.draw.rect(self.screen, color_show, [850, 120+i*20, 100, 20])
            pygame.display.update()
            
            
            