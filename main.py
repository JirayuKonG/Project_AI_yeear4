import threading
import pygame
from sys import exit
import sys
import time

from ui import Button , Grid , DynamicSizeObject
import  utils
import game

pygame.init()  # เริ่มต้นโมดูลของ pygame   to start pygame 

# สร้างหน้าจอเกม   Space surface
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)   # draw border of game   show for 1 frame
pygame.display.set_caption("15 PUzzle!")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)


# Set the background color (RGB: Red, Green, Blue)
BACKGROUND_COLOR = GREY  # Gray

# Fonts
font = pygame.font.Font(None, 40)


GRID_SIZE = 4 # ขนาดของกริด 4x4 = 16 ช่อง  


# ขนาดช่อง    ของเเต่ละช่่องง grid 
CELL_SIZE = 600 // GRID_SIZE  #  => 600 // 4 => 150


def getGrid_size():
    return  GRID_SIZE

def getCell_size():
    return  CELL_SIZE


def main ():
    
    
    # สร้างหน้าจอเกม   Space surface
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)   # draw border of game   show for 1 frame
    pygame.display.set_caption("15 PUzzle!")
    
    # Create a button (position: x=300, y=250, width=200, height=80)   create object 
    button_start1 = Button( (SCREEN_WIDTH / 2) -230 , SCREEN_HEIGHT / 4 , 600, 80, "Start Game 1st")
    button_start2 = Button( (SCREEN_WIDTH / 2) -230 , SCREEN_HEIGHT / 2.5, 600, 80, "Start Game 1st Vs Bot using ai algorithm")
    button_quit = Button( (SCREEN_WIDTH / 2) -230 , SCREEN_HEIGHT / 1.75 , 600, 80, "Quit Game")

    
    
    move_index = 1  # เริ่มที่การเคลื่อนไหวครั้งแรก
    move_count = 0  # ตัวแปรสำหรับนับการเคลื่อนไหว
    
    
    clock = pygame.time.Clock()
    last_move_time = time.time()
    end_time = None  # เก็บค่าเวลาที่เกมจบ
    
    count_game1_empty = 1 
    
    # เริ่มเกมลูป
    running = True      
    # draw all our elements
    # update everything
    while running:

        
        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)
        

        # Draw buttons
        button_start1.draw(screen)
        button_start2.draw(screen)
        button_quit.draw(screen)
        
        #       this part will get all that event all
        for event in pygame.event.get():
            #                V 
            if event.type == pygame.QUIT:  # for checking to cloas a game window 
                running = False
                pygame.quit()  # to close the pygame.init() 
                exit()
            elif event.type == pygame.VIDEORESIZE:  # Handle screen resize
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:   
                
                
                if button_start1.is_clicked(event.pos):
                    print("Start Game 1st button clicked!")
                    screen.fill(BACKGROUND_COLOR)
                    
                    while True: 
                        listNumber_1 =  utils.ListNumber(GRID_SIZE)
                        numbers_1 = listNumber_1.randomNumber()
                        if listNumber_1.is_solvable(numbers_1):
                            break
                    
                    gameRunning = True
                    while gameRunning :
                        # return false
                        gameRunning = game.gamePlayer_loop(numbers_1,screen)               
                        
                
                if button_start2.is_clicked(event.pos):
                    print("Start Game 1st vs ai algor button clicked!")
                    
                    # สร้างหน้าจอเกม   Space surface
                    SCREEN_WIDTH_2P = SCREEN_WIDTH + 300
                    SCREEN_HEIGHT_2P = SCREEN_HEIGHT + 300
                    screen = pygame.display.set_mode((SCREEN_WIDTH_2P, SCREEN_HEIGHT_2P), pygame.RESIZABLE)   # draw border of game   show for 1 frame
                    pygame.display.set_caption("15 PUzzle!")
                    
                    screen.fill(BACKGROUND_COLOR)
                

                    while True:
                        listNumber_2 =  utils.ListNumber(GRID_SIZE)
                        numbers_2 = listNumber_2.randomNumber()
                        # the numbers_2 will use to race between human and bot(ai) using a * algorithm
                        if listNumber_2.is_solvable(numbers_2):
                            break
                    
                    # Create both threads      (look an object)-------------------------------
                    # player_thread = threading.Thread(target=game.gamePlayer_loop_2(numbers_2,screen))
                    # algorithm_thread = threading.Thread(target=game.gameAlgorithm_loop(numbers_2,screen))
                    
                    # Start both threads--------------------------------------
                    # player_thread.start()
                    # algorithm_thread.start()
                    
                    # Wait for threads to finish---------------------------
                    # player_thread.join()
                    # algorithm_thread.join()
                    
                    
                    
                    # sys.exit()  close the program  ===>   pygame.init()
                    
                    # maybe not use
                    gameRunning = True
                    while gameRunning :
                        # return false
                        gameRunning = game.gamePlayer_loop_2(numbers_2,screen)  
                    
                
                if button_quit.is_clicked(event.pos):
                    print("Quit Game button clicked!")
                    pygame.quit()
                    sys.exit()
                
                    
                        
        drawObject_display = DynamicSizeObject(SCREEN_WIDTH,SCREEN_HEIGHT)
        # button_start1 , button_start2 , button_quit = drawObject_display.draw_dynamic()
        
        # Draw objects that scale with the screen size
        # draw_dynamic_objects(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # button_start1.draw(screen)
        # button_start2.draw(screen)
        # button_quit.draw(screen)
        
        
        pygame.display.update() # update the screen that color 200 200 200
        
        # Update the display
        pygame.display.flip()
        
        clock.tick(60)
        
        

if __name__ == '__main__':
    print("START PROGRAM !!!")
    main()
    
    



