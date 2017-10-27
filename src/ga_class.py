from numpy import *
from numpy.random import *


class ga_class:
    
    
    def __init__(self):
        self.num_generation = 5
        self.now_generation = 1
        self.num_params     = 33
        self.num_curtain    = 30
        self.set_params_text()
        self.generate_curtains()

    
    def set_params_text(self):
        self.params_text =[\
                           'surf_alpha',\
                           'back_r',\
                           'back_g',\
                           'back_b',\
                           'back_have_pattern',\
                           'back_pattern_adjust_rgb',\
                           'back_pattern_rect_or_line',\
                           'rect_h_num',\
                           'rect_v_num',\
                           'line_num',\
                           'line_width_min',\
                           'line_width_max',\
                           'line_length_min',\
                           'line_length_max',\
                           'line_direction',\
                           'line_start_side',\
                           'line_start_pos',\
                           'line_range',\
                           'line_or_lines',\
                           'lines_points',\
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
                           'fore_h_num',\
                           'fore_v_num',\
                           'fore_pattern_size'\
                           ]
    
     
    def generate_curtains(self):
        for i in range(self.num_curtain):
            self.curtains[i] = self.create_random_params()
        if self.now_generation > 1: 
            pass
        
            
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
        params['back_pattern_rect_or_line'] = randint(101)    # rectangle or line pattern (%)
        # rectangle pattern
        params['rect_h_num']                = randint(1,20)   # rectangle number (horizontal direction)
        params['rect_v_num']                = randint(1,20)   # rectangle number (vertical direction)
        # line(or lines) pattern
        params['line_num']                  = randint(1,30)
        params['line_width_min']            = randint(1,50)   # (%)
        params['line_width_max']            = randint(51,101) # (%)
        params['line_length_min']           = randint(1,50)   # (%)
        params['line_length_max']           = randint(51,101) # (%)
        params['line_direction']            = randint(101)    # horizontal or vertical (%)
        params['line_start_side']           = randint(101)    # small side or large side (%)
        params['line_start_pos']            = randint(101)    # start position from start side (%)
        params['line_range']                = randint(101)    # line distribution range        
        params['line_or_lines']             = randint(101)    # (%)
        params['lines_points']              = randint(5,30)   # number of turning-points
        # foreground
        params['fore_have']                 = randint(101)    # has or do not have foreground (%)
        params['fore_kinds']                = randint(1,20)   # pattern kinds
        parems['ellipse_or_triangle']       = randint(101)    # (%)
        parems['fore_adjust_range_r']       = randint(1,200)
        parems['fore_adjust_range_g']       = randint(1,200)
        parems['fore_adjust_range_b']       = randint(1,200)
        parems['fore_h_start_lim']          = randint(1,50)   # upper limit of start (horizontal direction) (%)
        parems['fore_h_end_lim']            = randint(51,101) # lower limit of end (horizontal direction) (%)
        parems['fore_v_start_lim']          = randint(1,50)   # upper limit of start (vertical direction) (%)
        parems['fore_v_end_lim']            = randint(51,101) # lower limit of end (vertical direction) (%)
        params['fore_h_num']                = randint(1,15)   # number base of patterns (horizontal direction)
        params['fore_v_num']                = randint(1,15)   # number base of patterns (vertical direction)
        parems['fore_pattern_size']         = randint(30)     # is related to distribution area size  (%)
        return params       
