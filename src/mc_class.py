import os
import pygame
from numpy import *
from numpy.random import *
from ga_class import *

pygame.init()
pygame.font.init()

class mc_class:
    
    
    def __init__(self):
        self.name         = 'Magic Curtain'        
        self.root_path    = os.path.abspath('..')  
        self.flag_exit    = False
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
        if self.idx_step == 0 and not self.is_start:
            return
        # all message scene
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
                        self.flag_exit = flag_exit
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
                        if self.flag_exit:
                            return
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
            
            
    def create_show_params(self,curtain):
        params = {}
        # whole surface
        params['surf_alpha'] = curtain['surf_alpha']
        # background
        params['back_color'] = (curtain['back_r'],\
                                curtain['back_g'],\
                                curtain['back_b'])
        if params['back_color'] == (0, 0, 0):
            params['back_color'] = (1, 1, 1)
        if curtain['back_have_pattern'] < 50:
            params['back_have_pattern'] = False
        else:
            params['back_have_pattern'] = True
        # rectangle
        if curtain['rect_or_line'] < 50:
            params['rect_or_line'] = False
        else:
            params['rect_or_line'] = True
        params['rect_color'] = (min(255,max(0,curtain['back_r'] + curtain['back_pattern_adjust_rgb'])),\
                                min(255,max(0,curtain['back_g'] + curtain['back_pattern_adjust_rgb'])),\
                                min(255,max(0,curtain['back_b'] + curtain['back_pattern_adjust_rgb'])))
        if params['rect_color'] == (0, 0, 0):
            params['rect_color'] = (1, 1, 1)
        params['rect_witdh'] = self.size_curtain[0] / 2 / curtain['rect_h_num']
        params['rect_height'] = self.size_curtain[1] / curtain['rect_v_num']
        params['rect_h_num'] = curtain['rect_h_num']
        params['rect_v_num'] = curtain['rect_v_num']
        # line
        if curtain['line_direction'] < 50:
            params['line_direction'] = False
            curtain_range = 300
            params['line_num'] = int(curtain['line_num'])
        else:
            params['line_direction'] = True
            curtain_range = 600
            params['line_num'] = int(curtain['line_num']) * 2
        if curtain['line_start_side'] < 50:
            params['line_start_side'] = False
            line_range_start = 0
            line_range_end = curtain_range * curtain['line_range'] / 100
        else:
            params['line_start_side'] = True
            line_range_start = curtain_range * ( 1 - curtain['line_range'] / 100 )
            line_range_end = curtain_range
        line_range = line_range_end - line_range_start + 1
        line_step = line_range / params['line_num']
        if line_step <1:
            line_step = 1
        if curtain['line_or_lines'] < 50:
            params['line_or_lines'] = False
        else:
            params['line_or_lines'] = True
        params['line'] = []                                                
        for i in range(params['line_num']):            
            params['line'].append([]) 
            params['line'][i] = {}
            line_color = randint(-curtain['back_pattern_adjust_rgb'], curtain['back_pattern_adjust_rgb'])
            params['line'][i]['color'] = (\
                  min(255,max(0, curtain['back_r'] + line_color )),\
                  min(255,max(0, curtain['back_g'] + line_color )),\
                  min(255,max(0, curtain['back_b'] + line_color )))
            if params['line'][i]['color'] == (0, 0, 0):
                params['line'][i]['color'] = (1, 1, 1)
#            print(line_range_start )
#            print(line_step)
            line_pos_bias = randint( line_range_start + line_step*i, line_range_start + line_step*(i+1) )          
            line_length = randint( curtain['line_length_min'], curtain['line_length_max'])
            if line_step * curtain['line_width_max'] - 100 - line_step * curtain['line_width_min'] / 100 < 1:
                params['line'][i]['width'] = randint( line_step * curtain['line_width_min'] / 100, line_step * curtain['line_width_min'] / 100 + 1)
            else:
                params['line'][i]['width'] = randint( line_step * curtain['line_width_min'] / 100, line_step * curtain['line_width_max'] / 100)                
            if params['line_direction']:
                if params['line_start_side']:
                    params['line'][i]['start_point'] = ( 300 * ( 1 - line_length / 100 ), line_pos_bias )
                    params['line'][i]['end_point'] = ( 300, line_pos_bias ) 
                else:
                    params['line'][i]['start_point'] = ( 0, line_pos_bias)
                    params['line'][i]['end_point'] = ( 300 * line_length / 100, line_pos_bias)                        
            else:
                if params['line_start_side']:
                    params['line'][i]['start_point'] = ( line_pos_bias, 600 * ( 1 - line_length / 100 ))
                    params['line'][i]['end_point'] = ( line_pos_bias, 600 )
                else:
                    params['line'][i]['start_point'] = ( line_pos_bias, 0 )
                    params['line'][i]['end_point'] = ( line_pos_bias, 600 * line_length / 100 )
            params['line'][i]['turning_points'] = randint(1,curtain['lines_turning_points'])
        # foreground
        if curtain['fore_have'] < 50:
            params['fore_have'] = False
        else:
            params['fore_have'] = True
        params['fore_kinds'] = curtain['fore_kinds']
        params['fore'] = []  
        for i in range(params['fore_kinds']):            
            params['fore'].append([]) 
            params['fore'][i] = {}
            params['fore'][i]['ellipse_or_triangle'] = ( randint(101) < curtain['ellipse_or_triangle'])
            fore_color = []
            fore_color.append(randint( -curtain['fore_adjust_range_r'], curtain['fore_adjust_range_r']))
            fore_color.append(randint( -curtain['fore_adjust_range_g'], curtain['fore_adjust_range_g']))
            fore_color.append(randint( -curtain['fore_adjust_range_b'], curtain['fore_adjust_range_b']))
            params['fore'][i]['color'] = (\
                  int(min(255,max(0, curtain['back_r'] + fore_color[0]))),\
                  int(min(255,max(0, curtain['back_g'] + fore_color[1]))),\
                  int(min(255,max(0, curtain['back_b'] + fore_color[2]))))
            if params['fore'][i]['color'] == (0, 0, 0):
                params['fore'][i]['color'] = (1, 1, 1)
            params['fore'][i]['h_start'] = 300 * randint( curtain['fore_h_start_lim'] )/100
            params['fore'][i]['h_end'] = 300 * randint( curtain['fore_h_end_lim'], 100 )/100   
            params['fore'][i]['v_start'] = 600 * randint( curtain['fore_v_start_lim'] )/100
            params['fore'][i]['v_end'] = 600 * randint( curtain['fore_v_end_lim'], 100 )/100
            params['fore'][i]['h_num'] = randint( curtain['fore_h_num_base'] * 0.5, curtain['fore_h_num_base'] * 1.5 )     
            params['fore'][i]['v_num'] = randint( curtain['fore_v_num_base'] * 0.5, curtain['fore_v_num_base'] * 1.5 ) 
            params['fore'][i]['size'] = randint( curtain['fore_pattern_size_base'] * 0.5, curtain['fore_pattern_size_base'] * 1.5 )  
        return params
      
    
    def show_curtain(self, show_params): 
        self.screen.blit(self.img_curtain, (0,0))
        self.screen.blit(self.surf_window, (0,0))
        self.screen.blit(self.surf_wall, (0,0))        
        surf_curtain = pygame.Surface((self.size_curtain[0], self.size_curtain[1]))
        surf_curtain.fill(show_params['back_color'])
        surf_pattern = pygame.Surface((self.size_curtain[0]/2, self.size_curtain[1]))
        surf_pattern.fill(self.color_key)
        # draw background
        if show_params['back_have_pattern']:
            if show_params['rect_or_line']:
                for i  in range(int(show_params['rect_h_num'])):
                    for j  in range(int(show_params['rect_v_num'])):
                        if i % 2:
                            pygame.draw.rect(surf_pattern, show_params['rect_color'],\
                                             [show_params['rect_witdh']*i, show_params['rect_height']*j,\
                                              show_params['rect_witdh'], show_params['rect_height']/2])
                        else:
                            pygame.draw.rect(surf_pattern, show_params['rect_color'],\
                                             [show_params['rect_witdh']*i, show_params['rect_height']*j+show_params['rect_height']/2,\
                                              show_params['rect_witdh'], show_params['rect_height']/2])
            else:
                for i in range(int(show_params['line_num'])):
                    if show_params['line_or_lines']:
                        pygame.draw.line(surf_pattern, show_params['line'][i]['color'],\
                                         show_params['line'][i]['start_point'],\
                                         show_params['line'][i]['end_point'],\
                                         show_params['line'][i]['width'])
                    else:
                        turning_points = []
                        turning_points.append( show_params['line'][i]['start_point'] ) 
                        if show_params['line_direction']:
                            tmp = show_params['line'][i]['start_point'][0]
                            for j in range(show_params['line'][i]['turning_points']):                        
                                if show_params['line_start_side']: 
                                    tmp = tmp + (show_params['line'][i]['end_point'][0] - show_params['line'][i]['start_point'][0]) * 2**(-j-1)                                    
                                else:
                                    tmp = show_params['line'][i]['start_point'][0] +\
                                          (show_params['line'][i]['end_point'][0] - show_params['line'][i]['start_point'][0]) *\
                                           2**(j-show_params['line'][i]['turning_points'])
                                if j % 2:
                                    turning_points.append( (tmp, show_params['line'][i]['start_point'][1] - show_params['line'][i]['width'] / 2))
                                else:
                                    turning_points.append( (tmp, show_params['line'][i]['start_point'][1] + show_params['line'][i]['width'] / 2)) 
                        else:
                            tmp = show_params['line'][i]['start_point'][1]       
                            for j in range(show_params['line'][i]['turning_points']):
                                if show_params['line_start_side']: 
                                    tmp = tmp + (show_params['line'][i]['end_point'][1] - show_params['line'][i]['start_point'][1]) * 2**(-j-1)
                                else:
                                    tmp = show_params['line'][i]['start_point'][1] +\
                                          (show_params['line'][i]['end_point'][1] - show_params['line'][i]['start_point'][1]) *\
                                          2**( j - show_params['line'][i]['turning_points'])
                                if j % 2:
                                    turning_points.append( (show_params['line'][i]['start_point'][0] - show_params['line'][i]['width'], tmp))
                                else:
                                    turning_points.append( (show_params['line'][i]['start_point'][0] + show_params['line'][i]['width'], tmp) ) 
                        turning_points.append( show_params['line'][i]['end_point'] )             
                        pygame.draw.lines(surf_pattern, show_params['line'][i]['color'],\
                                          False, turning_points, show_params['line'][i]['width']) 
        # draw foreground
        if show_params['fore_have']:
            for i in range(show_params['fore_kinds']):
                fore_width = show_params['fore'][i]['h_end']-show_params['fore'][i]['h_start']
                fore_height = show_params['fore'][i]['v_end']-show_params['fore'][i]['v_start']
                if show_params['fore'][i]['ellipse_or_triangle']:
                    for j in range(int(show_params['fore'][i]['h_num'])):
                        for k in range(int(show_params['fore'][i]['v_num'])):
                            pygame.draw.ellipse(surf_pattern,show_params['fore'][i]['color'], \
                                                [show_params['fore'][i]['h_start'] + j * fore_width / show_params['fore'][i]['h_num'], \
                                                 show_params['fore'][i]['v_start'] + k * fore_height / show_params['fore'][i]['v_num'], \
                                                 fore_width * show_params['fore'][i]['size'] / 100, \
                                                 fore_height * show_params['fore'][i]['size'] / 200 ])
                else:
                    for j in range(int(show_params['fore'][i]['h_num'])):
                        for k in range(int(show_params['fore'][i]['v_num'])):
                            base_pose = (show_params['fore'][i]['h_start'] + j * fore_width / show_params['fore'][i]['h_num'],\
                                         show_params['fore'][i]['v_start'] + k * fore_height / show_params['fore'][i]['v_num']);
                            pygame.draw.polygon(surf_pattern,show_params['fore'][i]['color'], \
                                                [(base_pose[0]+fore_width * show_params['fore'][i]['size'] / 100,base_pose[1] + fore_height * show_params['fore'][i]['size'] / 200),\
                                                 (base_pose[0]+fore_width * show_params['fore'][i]['size'] / 200,base_pose[1]),\
                                                 (base_pose[0],base_pose[1]+fore_height * show_params['fore'][i]['size'] / 400)])
        surf_pattern.set_colorkey(self.color_key)
        surf_pattern.set_alpha(255) 
        surf_curtain.blit(surf_pattern, (0, 0))        
        surf_curtain.blit(pygame.transform.flip(surf_pattern,True,False), (300, 0))    
        surf_curtain.blit(self.mask_curtain, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
        surf_curtain.set_colorkey(self.color_key)
        surf_curtain.set_alpha(show_params['surf_alpha']) 
        self.screen.blit(surf_curtain, (0,0))       


    def get_score(self, idx_curtain, flag_click_enable):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()    
        surf_score = pygame.Surface((400, 600))
        surf_score.fill(self.color['white'])
        # draw rule
        pygame.draw.line(surf_score,self.color['black'],(150,150),(150,550),10)
        pygame.draw.line(surf_score,self.color['black'],(130,145),(170,145),10)
        pygame.draw.line(surf_score,self.color['black'],(130,555),(170,555),10)        
        str_num = 'please score No.'+str(idx_curtain+1)+' curtain'
        surf_text, rect_text = self.text_object(str_num,'comicsansms',25, self.color['black'])
        rect_text.center = (200,30)
        surf_score.blit(surf_text, rect_text)        
        surf_text, rect_text = self.text_object('by clicking on the rule' + '(of ' +str(self.ga.num_curtain) +')','comicsansms',25, self.color['black'])
        rect_text.center = (200,80)
        surf_score.blit(surf_text, rect_text)
        surf_text, rect_text = self.text_object('100','comicsansms',50, self.color['black'])
        rect_text.center = (70,145)
        surf_score.blit(surf_text, rect_text) 
        surf_text, rect_text = self.text_object('   0','comicsansms',50, self.color['black'])
        rect_text.center = (75,555)
        surf_score.blit(surf_text, rect_text)         
        for i in range(4):
            pygame.draw.line(surf_score, self.color['black'],(140,230+80*i),(160,230+80*i),2)
            surf_text, rect_text = self.text_object(str(100-(i+1)*20),'comicsansms',20, self.color['black'])
            rect_text.center = (95,230+80*i)
            surf_score.blit(surf_text, rect_text)
        if 730<mouse_x<770 and 149<mouse_y<551:
            surf_score.blit(self.img_heart,(125,mouse_y-25))          
            surf_text, rect_text = self.text_object(str(100 - (mouse_y-150)/4),'comicsansms',70, self.color['black'])
            rect_text.center = (290,mouse_y)
            surf_score.blit(surf_text, rect_text)
            if pygame.mouse.get_pressed()[0]:
                if flag_click_enable:
                    self.ga.scores.append(100 - (mouse_y-150)/4)
                    return True
        self.screen.blit(surf_score,(600,0))
        pygame.display.update()
        return False
    
    
    def score_curtain(self):
        if self.idx_step == 1:
            seed(1)
#            seed(pygame.time.get_ticks())
            self.ga = ga_class()
        else:
            self.ga.now_generation += 1
            self.ga.num_curtain = 10
            self.ga.generate_curtains()
        self.ga.scores = []
        self.screen.fill(self.color['white'])        
        for idx_curtain in range(self.ga.num_curtain):
            show_params = self.create_show_params(self.ga.curtains[idx_curtain])            
            flag_click_enable = False
            time_start = pygame.time.get_ticks()
            while True:
                time_now = pygame.time.get_ticks()
                if not flag_click_enable:
                    if time_now - time_start > 300:
                        flag_click_enable = True
                for event in pygame.event.get():                      
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.exit_box()
                            if self.flag_exit:
                                return
                self.show_curtain(show_params)            
                flag_get = self.get_score(idx_curtain, flag_click_enable)
                if flag_get:
                    flag_click_enable = False
                    break                   
                
                
    def show_result(self):
        self.ga.num_curtain = 1
        self.ga.generate_curtains()
        show_params = self.create_show_params(self.ga.curtains[0])
        flag_save = True
        while True:
            for event in pygame.event.get():                      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit_box()
                        if self.flag_exit:
                            return
            self.screen.fill(self.color['white'])
            self.show_curtain(show_params)
            surf_text, rect_text = self.text_object('I guess you like this.','comicsansms',30, self.color['black'])
            rect_text.center = (800,200)
            self.screen.blit(surf_text, rect_text)
            surf_text, rect_text = self.text_object('And the curtain image','comicsansms',30, self.color['black'])
            rect_text.center = (800,300)
            self.screen.blit(surf_text, rect_text)
            surf_text, rect_text = self.text_object(' has been saved.','comicsansms',30, self.color['black'])
            rect_text.center = (800,400)
            self.screen.blit(surf_text, rect_text)
            pygame.display.update()            
            if flag_save:
                pygame.image.save(self.screen, os.path.join(self.root_path, 'res.jpg'))
                flag_save = False
        