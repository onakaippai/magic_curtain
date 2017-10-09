#show image

import pygame

pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('Magic Curtain')
clock = pygame.time.Clock()
white = (255, 255, 255)

imgpath = 'D:/source/magic_curtain/img_pattern/'
bg = pygame.image.load(imgpath + 'background.png')
gara = pygame.image.load(imgpath + 'gara.png')
bg_mask = pygame.image.load(imgpath + 'background_mask.png')
curtain_mask = pygame.image.load(imgpath + 'curtain_mask.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill((white)) 
    screen.blit(bg,(50,50))
    temp = pygame.Surface((gara.get_width(), gara.get_height())).convert()
    temp.blit(gara, (0, 0))
    temp.blit(curtain_mask, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)  
    temp.set_colorkey((0,0,0))
    temp.set_alpha(128) 
    screen.blit(temp, (50,50))
    
    
    pygame.display.update()
    clock.tick(60)