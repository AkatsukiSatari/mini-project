import pygame
from random import randint

pygame.init()
WIDTH = 400
HEIGHT = 600
man_hinh = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flopy borb')

run_game = True
background = pygame.image.load('sky.png')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))

clock = pygame.time.Clock()


#cột information
blue = (0, 0, 225)

TUBE_WIDTH = 50
TUBE_VELOCITY = 2
TUBE_RANGE = 150

tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

tube1_x = 400
tube2_x = 600
tube3_x = 800

# duyệt biến
tube1_pass = False
tube2_pass = False
tube3_pass = False

freeze = False
dk_use_R = False

#bách- ko di chuyển
pink = (255,141,161)
BACH_WIDTH = 40
BACH_HEIGHT = 40
GRAVITY = 0.5
bach_drop_velocity = 0

bach_img = pygame.image.load('monkey.png')
bach_img = pygame.transform.scale(bach_img,(40, 40))
bach_x = 50
bach_y = 300


#điểm
black = (0, 0, 0)
score = 0
font = pygame.font.SysFont('sans', 20)

while run_game:
    clock.tick(60)
    man_hinh.blit(background,(0,0))
    
    #cống
    tube1 = pygame.draw.rect(man_hinh, blue, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    tube2 = pygame.draw.rect(man_hinh, blue, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    tube3 = pygame.draw.rect(man_hinh, blue, (tube3_x, 0, TUBE_WIDTH, tube3_height))
    
    #cống ngược
    tube1_ngc = pygame.draw.rect(man_hinh, blue, (tube1_x, TUBE_RANGE + tube1_height, TUBE_WIDTH, HEIGHT - TUBE_RANGE))
    tube2_ngc = pygame.draw.rect(man_hinh, blue, (tube2_x, TUBE_RANGE + tube2_height, TUBE_WIDTH, HEIGHT - TUBE_RANGE))
    tube3_ngc = pygame.draw.rect(man_hinh, blue, (tube3_x, TUBE_RANGE + tube3_height, TUBE_WIDTH, HEIGHT - TUBE_RANGE))
    
    #bách
    bach = man_hinh.blit(bach_img,(bach_x, bach_y))
    bach_y += bach_drop_velocity
    bach_drop_velocity += GRAVITY
    
    #vận tốc ống
    tube1_x -= TUBE_VELOCITY
    tube2_x -= TUBE_VELOCITY
    tube3_x -= TUBE_VELOCITY
    
    #điểm 
    score_txt = font.render('social creadit: ' + str(score), True, black)
    man_hinh.blit(score_txt, (0,0) )
    
    #tính điểm
    if bach_x >= tube1_x and tube1_pass == False:
        score += 1 
        tube1_pass = True
        
    if bach_x >= tube2_x and tube2_pass == False:
        score += 1 
        tube2_pass = True
        
    if bach_x >= tube3_x and tube3_pass == False:
        score += 1 
        tube3_pass = True
    
    # reuse cột
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550 
        tube1_height = randint(100, 400)
        tube1_pass = False
        
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False
        
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550 
        tube3_height = randint(100, 400) 
        tube3_pass = False    
    
    #collision
    for i in [tube1, tube2, tube3, tube1_ngc, tube2_ngc, tube3_ngc]:
        if bach.colliderect(i):
            dk_use_R = True
            freeze = True
            TUBE_VELOCITY = 0
            bach_drop_velocity = 0    
            game_over_txt = font.render("Game Over, Your social creadit: " + str(score), True, black)
            man_hinh.blit(game_over_txt, (100, 300))
            press_R = font.render("Press R to try again", True, black)
            man_hinh.blit(press_R, (100, 320))
            
    if bach_y > 600:
        dk_use_R = True
        freeze = True
        TUBE_VELOCITY = 0
        bach_drop_velocity = 0    
        game_over_txt = font.render("Game Over, Your social creadit: " + str(score), True, black)
        man_hinh.blit(game_over_txt, (100, 300))
        press_R = font.render("Press R to try again", True, black)
        man_hinh.blit(press_R, (100, 320))  
    elif bach_y < -50:
        dk_use_R = True
        freeze = True
        TUBE_VELOCITY = 0
        bach_drop_velocity = 0    
        game_over_txt = font.render("Game Over, Your social creadit: " + str(score), True, black)
        man_hinh.blit(game_over_txt, (100, 300))
        press_R = font.render("Press R to try again", True, black)
        man_hinh.blit(press_R, (100, 320))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and freeze == False:
                bach_drop_velocity = 0
                bach_drop_velocity -= 8
        if event.type == pygame.KEYDOWN and dk_use_R == True:
            if event.key == pygame.K_r:
                freeze = False
                dk_use_R = False
                tube1_height = randint(100,400)
                tube2_height = randint(100,400)
                tube3_height = randint(100,400)
                bach_y = 300
                tube1_x = 400
                tube2_x = 600
                tube3_x = 800
                bach_drop_velocity = 0
                bach_drop_velocity -= 8
                score = 0
                TUBE_VELOCITY = 2
        
                
    
    pygame.display.flip()
    
pygame.quit()