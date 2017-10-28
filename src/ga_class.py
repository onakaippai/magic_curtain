from numpy import *
from numpy.random import *


class ga_class:
    
    
    def __init__(self):
        self.num_generation = 5
        self.now_generation = 1
        self.num_params     = 33
        self.num_curtain    = 30
        self.set_text_params()
        self.generate_curtains()

    
    def set_text_params(self):
        self.text_params =[\
                           'surf_alpha',\
                           'back_r',\
                           'back_g',\
                           'back_b',\
                           'back_have_pattern',\
                           'back_pattern_adjust_rgb',\
                           'rect_or_line',\
                           'rect_h_num',\
                           'rect_v_num',\
                           'line_num',\
                           'line_width_min',\
                           'line_width_max',\
                           'line_length_min',\
                           'line_length_max',\
                           'line_direction',\
                           'line_start_side',\
                           'line_position',\
                           'line_range',\
                           'line_or_lines',\
                           'lines_turning_points',\
                           'fore_have',\
                           'fore_kinds',\
                           'ellipse_or_triangle',\
                           'fore_adjust_range_r',\
                           'fore_adjust_range_g',\
                           'fore_adjust_range_b',\
                           'fore_h_start_lim',\
                           'fore_h_end_lim',\
                           'fore_v_start_lim',\
                           'fore_v_end_lim',\
                           'fore_h_num_base',\
                           'fore_v_num_base',\
                           'fore_pattern_size_base'\
                           ]
    
     
    def generate_curtains(self):
        if self.now_generation == 1: 
            self.curtains = []
            self.cross_rate = 0.6
            self.mutate_rate = 0.15
            for i in range(self.num_curtain):
                self.curtains.append(self.create_random_params())
#                self.curtains[i] = self.create_random_params()                
        else: 
            curtain_rank = sorted(self.scores, reverse=True)
            parents = []
            parents.append(self.curtains[self.scores.index(curtain_rank[0])])
            parents.append(self.curtains[self.scores.index(curtain_rank[1])])
            parents.append(self.curtains[self.scores.index(curtain_rank[2])])
#            parents[0] = self.curtains[self.scores.index(curtain_rank[0])]
#            parents[1] = self.curtains[self.scores.index(curtain_rank[1])]
#            parents[2] = self.curtains[self.scores.index(curtain_rank[2])] 
            self.curtains = []
            for i in range(self.num_curtain):
                if i < 3:
                    self.curtains.append(parents[i])
                else:
                    self.curtains.append(self.create_random_params())
                    for j in range(self.num_params):
                        if rand() > self.mutate_rate:
                            if rand() > self.cross_rate:
                                self.curtains[i][self.text_params[j]] = parents[0][self.text_params[j]]
                            else:
                                self.curtains[i][self.text_params[j]] = parents[1][self.text_params[j]]
        
            
    def create_random_params(self):
        params = {}
        # whole surface
        params['surf_alpha']                = randint(180)    # curtain surface transparent rate
        # background        
        params['back_r']                    = randint(256)
        params['back_g']                    = randint(256)
        params['back_b']                    = randint(256)        
        params['back_have_pattern']         = randint(101)    # has or do not have pattern
        params['back_pattern_adjust_rgb']   = randint(1,200)
        params['rect_or_line']              = randint(101)    # rectangle or line pattern (%)
        # rectangle pattern
        params['rect_h_num']                = randint(1,20)   # rectangle number (horizontal direction)
        params['rect_v_num']                = randint(1,20)   # rectangle number (vertical direction)
        # line(or lines) pattern
        params['line_num']                  = randint(1,30)
        params['line_width_min']            = randint(1,50)   # (%)
        params['line_width_max']            = randint(51,100) # (%)
        params['line_length_min']           = randint(1,50)   # (%)
        params['line_length_max']           = randint(51,100) # (%)
        params['line_direction']            = randint(101)    # horizontal or vertical (%)
        params['line_start_side']           = randint(101)    # small side or large side (%)
        params['line_position']             = randint(101)    # start position (%)
        params['line_range']                = randint(101)    # line distribution range        
        params['line_or_lines']             = randint(101)    # (%)
        params['lines_turning_points']      = randint(5,30)   # number of turning-points
        # foreground
        params['fore_have']                 = randint(101)    # has or do not have foreground (%)
        params['fore_kinds']                = randint(1,20)   # pattern kinds
        params['ellipse_or_triangle']       = randint(101)    # (%)
        params['fore_adjust_range_r']       = randint(1,200)
        params['fore_adjust_range_g']       = randint(1,200)
        params['fore_adjust_range_b']       = randint(1,200)
        params['fore_h_start_lim']          = randint(1,50)   # upper limit of start (horizontal direction) (%)
        params['fore_h_end_lim']            = randint(51,100) # lower limit of end (horizontal direction) (%)
        params['fore_v_start_lim']          = randint(1,50)   # upper limit of start (vertical direction) (%)
        params['fore_v_end_lim']            = randint(51,100) # lower limit of end (vertical direction) (%)
        params['fore_h_num_base']           = randint(1,15)   # number base of patterns (horizontal direction)
        params['fore_v_num_base']           = randint(1,15)   # number base of patterns (vertical direction)
        params['fore_pattern_size_base']    = randint(1,30)   # is related to distribution area size  (%)
        return params       
