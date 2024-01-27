import pygame
from sys import exit    

pygame.init()
screen = pygame.display.set_mode((768, 650))
pygame.display.set_caption("Demo Game")
game_clock = pygame.time.Clock()
font = pygame.font.Font('fonts/INKFREE.TTF', 60)
start_time = 0
time = 0
score = 0

#Timed score method

def timed_score():
    global score, time
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score = time
    score_surface = font.render(f'Score: {time}', False, (70, 130, 180))
    score_rect = score_surface.get_rect(center = (384, 50))
    pygame.draw.rect(screen, "Black", score_rect)
    screen.blit(score_surface, score_rect)

def startGame():
    while True:
        screen.fill((255, 255, 255))
        start_msg = font.render("Press Space to Start", False, (70, 130, 180))
        start_msg_rectangle = start_msg.get_rect(center = (384, 50))
        screen.blit(start_msg, start_msg_rectangle)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playGame()
        
        # updates display
        pygame.display.flip()

def playGame():
    global start_time
    global score
    
    bg_1 = pygame.image.load('art/bg/background1.png')
    bg_2 = pygame.image.load('art/bg/background2.png')
    bg_3 = pygame.image.load('art/bg/background3.png')
    bg_4 = pygame.image.load('art/bg/background4.png')
    bg_5 = pygame.image.load('art/bg/background5.png')
    bg_6 = pygame.image.load('art/bg/background6.png')
    bg_7 = pygame.image.load('art/bg/background7.png')
    bg_8 = pygame.image.load('art/bg/background8.png')
    bg_9 = pygame.image.load('art/bg/background9.png')
    bg_10 = pygame.image.load('art/bg/background10.png')
    bg_11 = pygame.image.load('art/bg/background11.png')
    bg_12 = pygame.image.load('art/bg/background12.png')
    bg_13 = pygame.image.load('art/bg/background13.png')
    bg_14 = pygame.image.load('art/bg/background14.png')
    bg_15 = pygame.image.load('art/bg/background15.png')
    bg_change = [bg_1, bg_2, bg_3, bg_4, bg_5, bg_6, bg_7, bg_8, bg_9, bg_10, bg_11, bg_12, bg_13, bg_14, bg_15]
    bg_index = 0
    bg_surface = bg_change[bg_index]
    
    def bg_animated():
        nonlocal bg_surface, bg_index
        bg_index += 0.05
        if bg_index == 15:
            bg_index = 1 
        if bg_index > len(bg_change):
            bg_index = 0
        bg_surface = bg_change[int(bg_index)]
    
    map_surface = pygame.image.load('art/map.png').convert_alpha()


    obstacle_surface = pygame.image.load('art/obstacles/poop.png').convert_alpha()
    obstacle_rectangle = obstacle_surface.get_rect(bottomright = (770, 475))
    obstacle_rectangle.height = 51
    obstacle_rectangle.width = 40
    
    obstacle_rectangle_list = []

    player_walk_1 = pygame.image.load('art/player/totorowalk1.png')
    player_walk_2 = pygame.image.load('art/player/totorowalk2.png')
    player_walk_3 = pygame.image.load('art/player/totorowalk3.png')
    player_walk_4 = pygame.image.load('art/player/totorowalk4.png')
    player_walk_5 = pygame.image.load('art/player/totorowalk5.png')
    player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5]
    player_index = 0
    player_surface = player_walk[player_index]
    player_rectangle = player_surface.get_rect(bottomleft = (60, 430))
    player_rectangle.height = 65
    player_rectangle.width = 40
            
    def player_animated():
        nonlocal player_surface, player_index
        player_index += 0.2
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]
    
    player_gravity = 0
    game_run = True
    
    
    while True: 
        for event in pygame.event.get():
            global time, start_time
            if event.type == pygame.quit:
                pygame.quit()
                exit()
                
            if game_run:      
                if event.type == pygame.KEYDOWN:
                    # Jumping makes means negative gravity
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                        print("Jump")
                    elif event.key == pygame.K_s:
                        print("Duck")
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_run = True
                    obstacle_rectangle.x = 800
                    time = 0
                    score = 0
                    start_time = int(pygame.time.get_ticks() / 1000)

                
        if game_run:
            screen.blit(bg_surface, (0, 0))
            bg_animated()
            screen.blit(map_surface, (0, -60))
            
            # Using time as score instead
            timed_score()
        
            #obstacle moves to left and continuously appears on screen
            screen.blit(obstacle_surface, obstacle_rectangle)
            obstacle_rectangle.right -= 4
            if obstacle_rectangle.right <= 0:
                obstacle_rectangle.left = 770
            
            # Gravity increases while falling
            player_gravity += 1
            player_rectangle.y += player_gravity
            if player_rectangle.bottom >= 425:
                player_rectangle.bottom = 425
            player_animated()
            screen.blit(player_surface, player_rectangle)
            
            
            # Enemy colliding
            if player_rectangle.colliderect(obstacle_rectangle):
                game_run = False
            
        else: 
            obstacle_rectangle_list.clear()
            player_rectangle.bottomleft = (60, 430)
            player_gravity = 0
            screen.fill("SteelBlue")
            start_time = pygame.time.get_ticks()
            score_msg = font.render(f'Your Score: {score}', False, "Black")
            score_msg_rectangle = score_msg.get_rect(center = (384, 50))
            screen.blit(score_msg, score_msg_rectangle)
        
        pygame.display.update()
        game_clock.tick(60)
    
    
startGame()