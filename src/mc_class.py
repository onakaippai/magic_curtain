import os
import pygame
from numpy import *
from numpy.random import *


class mc_class:
    
    
    def __init__(self):
        self.name         = 'Magic Curtain'        
        self.root_path    = os.path.abspath('..')      
        self.size_screen  = (1000, 600) # [width, height]
        self.size_curtain = (600, 600)  # [width, height]        
        self.idx_season   = 0           # spring, summer, autumn, winter
        self.idx_wall     = 0           # white, light_gray, gray, hsv_order        
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((self.size_screen[0],self.size_screen[1]))
      
    
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
        
        
    def text_object(self, text, type_font, size_font, color_text):
        font_text = pygame.font.SysFont(type_font,size_font)
        surf_text = font_text.render(text, True, color_text)
        return surf_text, surf_text.get_rect()
        
    def show_message(self):
        time_start = pygame.time.get_ticks()
        while True: 
            for event in pygame.event.get():
                pass
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
                rect_text.center = (self.size_screen[0]* 1/2, self.size_screen[0] * 1/2)
                surf_screen.blit(surf_text, rect_text)      
            else:                
                rect_text_upper.center = (self.size_screen[0]* 1/2, self.size_screen[0] * 1/3)
                rect_text_lower.center = (self.size_screen[0]* 1/2, self.size_screen[0] * 2/3)
                surf_screen.blit(surf_text_upper, rect_text_upper)
                surf_screen.blit(surf_text_lower, rect_text_lower)    
            surf_screen.set_colorkey(self.color_key)
            self.screen.blit(surf_screen,(0,0))
            pygame.display.update()
            cnt_time = now_time - time_start
            if self.idx_step == 0:
                if cnt_time < self.time_welcome[0]:
                    surf_screen.set_alpha( cnt_time / 5 )
                elif cnt_time > self.time_welcome[1]:
                    surf_screen.set_alpha( 255 - cnt_time / 5 )
                elif cnt_time > self.time_welcome[2]:
                    break
            else:
                if cnt_time > self.time_otherwise:
                    break