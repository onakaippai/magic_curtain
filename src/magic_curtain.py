from mc_class import *

mc = mc_class()

while True:
    mc.is_start = True
    mc.show_message()
    if mc.idx_step == 0:
        mc.main_menu()
    elif mc.flag_finish:
        mc.show_result()
    else:
        mc.score_curtain()
    mc.is_start = False
    mc.show_message()
    mc.idx_step += 1
    if mc.idx_step > mc.ag.generation_num:
        mc.flag_finish = True
        
pygame.quit()
quit()