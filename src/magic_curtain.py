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
    if mc.flag_exit:
        break
    mc.is_start = False
    mc.show_message()
    mc.idx_step += 1
    if mc.ga.now_generation > mc.ga.num_gen:
        mc.flag_finish = True
        
pygame.quit()
quit()