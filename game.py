import pygame
from sys import exit
import sys
import random
import time

from ui import Button , Grid , DynamicSizeObject
import solver
import main
import utils

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)




# SCREEN_WIDTH = main.SCREEN_WIDTH
# SCREEN_HEIGHT = main.SCREEN_HEIGHT
# GRID_SIZE = main.GRID_SIZE
# CELL_SIZE = main.CELL_SIZE
# BACKGROUND_COLOR = main.BACKGROUND_COLOR  # Gray
# font = main.font
# # numbers = main.numbers










def gamePlayer_loop( numbers, screen ):
    
    SCREEN_WIDTH = main.SCREEN_WIDTH
    SCREEN_HEIGHT = main.SCREEN_HEIGHT
    GRID_SIZE = main.GRID_SIZE
    CELL_SIZE = main.CELL_SIZE
    BACKGROUND_COLOR = main.BACKGROUND_COLOR  # Gray
    font = main.font
    numbers = numbers
    

    count_game1_empty = 1
    if count_game1_empty == 1 :
        empty_row, empty_col = GRID_SIZE - 1, GRID_SIZE - 1  # ช่องว่างเริ่มต้นที่มุมล่างขวา  ????  must fix this things 
        count_game1_empty = 2
             
                    
    start_time = time.time()
    clock = pygame.time.Clock()
    last_move_time = time.time()
    end_time = None  # เก็บค่าเวลาที่เกมจบ
    
    
    move_index =0
    move_count =0 
    
    
    grid_game1 = Grid(GRID_SIZE,CELL_SIZE,15,15)
    
    
    # button_restart = Button( (SCREEN_WIDTH / 2) +75 , (SCREEN_HEIGHT / 3)+220 , 200, 80, "Get new suffle" )
    button_back = Button( (SCREEN_WIDTH / 2) +75 , (SCREEN_HEIGHT / 2)+220 , 200, 80, "Back" )
                    
    
    game1_running = True
    while game1_running:
        # print("Game1 is running...")     #  having problem
        # time.sleep(1)
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        screen.fill(BACKGROUND_COLOR)
        
        # button_restart.draw(screen)
        button_back.draw(screen)
        
        # draw_grid()
        grid_game1.draw(screen,numbers)

        if not utils.check_win(numbers):
            # แสดงเวลาและจำนวนการเคลื่อนไหวแบบเรียลไทม์
            time_text = font.render(f"Time: {int(elapsed_time)}s", True, BLACK)
            moves_text = font.render(f"Moves: {move_count}", True, BLACK)
            screen.blit(time_text, (50, main.SCREEN_HEIGHT - 100))
            screen.blit(moves_text, (50, main.SCREEN_HEIGHT - 50))
        
        if utils.check_win(numbers):
            if end_time is None:  # ถ้าเกมเพิ่งจบ ให้บันทึกเวลาสุดท้ายที่ชนะ
                end_time = elapsed_time
            # แสดงข้อความ AI ชนะและจำนวนการเคลื่อนไหว
            win_text = font.render(f"YOU Wins! Time: {int(end_time)}s", True, BLUE)
            final_moves_text = font.render(f"Moves: {move_count}", True, BLUE)
            screen.blit(win_text, (50, SCREEN_HEIGHT - 100))
            screen.blit(final_moves_text, (50, SCREEN_HEIGHT - 50))
            
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() # return position in the display x , y 
                print(pos)
                row, col = utils.get_clicked_cell(pos)

                # ตรวจสอบว่าคลิกอยู่ในแถวหรือคอลัมน์เดียวกับช่องว่างหรือไม่
                if row == empty_row and col != empty_col:  # คลิกในแถวเดียวกัน
                    utils.shift_row(row, empty_col, col, numbers)
                    empty_col = col
                elif col == empty_col and row != empty_row:  # คลิกในคอลัมน์เดียวกัน
                    utils.shift_col(col, empty_row, row, numbers)
                    empty_row = row
                    
                # if button_restart.is_clicked(event.pos):
                #     print("KONG restart or new shuwwsfel")
                    # # สร้างลิสต์ตัวเลข (สุ่มเฉพาะ 15 ตัวแรก)
                    # numbers = list(range(1, GRID_SIZE * GRID_SIZE))  # สร้างลิสต์ตั้งแต่ 0 ถึง 15 มีทั้งหมด 16 ตัว เเต่ เลือกเเค่ 1-15  
                    # print(numbers) #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

                    # random.shuffle(numbers)  # สุ่มลำดับตัวเลข
                    # print(numbers) #  random  มีจำนวน 15 ตัว เเละตัวสุดท้ายคือข้างล่าง
                    # numbers.append(0)  # เพิ่มช่องว่าง (0) ในตำแหน่งสุดท้าย
                    
                elif button_back.is_clicked(event.pos):
                    print("KONG back game page 1")
                    game1_running = False

        if not utils.check_win(numbers) and time.time() - last_move_time > 0.17:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ai_numbers = solution_path[move_index]
                move_index += 1
                move_count += 1  # นับจำนวนครั้งที่ AI เลื่อนตำแหน่ง
                last_move_time = time.time()
            # else:
            #     ai_won = True  # ตั้งค่าให้ AI ชนะเมื่อสิ้นสุดเส้นทาง
    
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    return False












def gamePlayer_loop_2( numbers, screen ):
    
    SCREEN_WIDTH = main.SCREEN_WIDTH 
    SCREEN_HEIGHT = main.SCREEN_HEIGHT 
    GRID_SIZE = main.GRID_SIZE 
    CELL_SIZE = main.CELL_SIZE - 15
    BACKGROUND_COLOR = main.BACKGROUND_COLOR  # Gray
    font = main.font
    
    numbers_1 = numbers
    numbers_2 = numbers

    count_game1_empty = 1
    if count_game1_empty == 1 :
        empty_row, empty_col = GRID_SIZE - 1, GRID_SIZE - 1  # ช่องว่างเริ่มต้นที่มุมล่างขวา  ????  must fix this things 
        count_game1_empty = 2
             
                    
    clock = pygame.time.Clock()
    
    goal_state = solver.getGoalStage()
    ai_won = False
    last_move_time = time.time()
    
    solution_path = solver.ida_star_search(numbers_2, goal_state) # ส่วนที่ algorithm ใช้ในการคำนวณ /////////////////////////////////////////////////////////////
    
    move_index_player =0
    move_count_player =0 
    move_index_ai =0 
    move_count_ai =0 
    
    end_time = None  # เก็บค่าเวลาที่เกมจบ
    
    
    grid_game1 = Grid(GRID_SIZE,CELL_SIZE,15,15)
    grid_game2 = Grid(GRID_SIZE,CELL_SIZE,900,15)
    
    
    # button_restart = Button( (SCREEN_WIDTH / 2) -300 , (SCREEN_HEIGHT / 3)+400 , 200, 80, "Get new suffle" )
    button_back = Button( (SCREEN_WIDTH / 2) - 80 , (SCREEN_HEIGHT / 2)+280 , 200, 80, "Back" )
                    
    start_time = time.time()
    
    game1_running = True
    while game1_running:
        # print("Game2 is running...")   #  having problem
        # time.sleep(1)
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        screen.fill(BACKGROUND_COLOR)
        
        # button_restart.draw(screen)
        button_back.draw(screen)
        
        # draw_grid()
        grid_game1.draw(screen,numbers_1)
        grid_game2.draw(screen,numbers_2)


        if not utils.check_win(numbers_1):
            # แสดงเวลาและจำนวนการเคลื่อนไหวแบบเรียลไทม์
            time_text = font.render(f"Time: {int(elapsed_time)}s", True, BLACK)
            moves_text = font.render(f"Moves: {move_count_player}", True, BLACK)
            screen.blit(time_text, (50, main.SCREEN_HEIGHT - 100))
            screen.blit(moves_text, (50, main.SCREEN_HEIGHT - 50))
        
        if utils.check_win(numbers_1):
            if end_time is None:  # ถ้าเกมเพิ่งจบ ให้บันทึกเวลาสุดท้ายที่ชนะ
                end_time = elapsed_time
            # แสดงข้อความ AI ชนะและจำนวนการเคลื่อนไหว
            win_text = font.render(f"YOU Wins! Time: {int(end_time)}s", True, BLUE)
            final_moves_text = font.render(f"Moves: {move_count_player}", True, BLUE)
            screen.blit(win_text, (50, SCREEN_HEIGHT - 100))
            screen.blit(final_moves_text, (50, SCREEN_HEIGHT - 50))
            
            
            
        if not ai_won:
            # แสดงเวลาและจำนวนการเคลื่อนไหวแบบเรียลไทม์
            time_text = font.render(f"Time: {int(elapsed_time)}s", True, BLACK)
            moves_text = font.render(f"Moves: {move_count_ai}", True, BLACK)
            screen.blit(time_text, (900, SCREEN_HEIGHT - 100))
            screen.blit(moves_text, (900, SCREEN_HEIGHT - 50))

        if ai_won:
            if end_time is None:  # ถ้าเกมเพิ่งจบ ให้บันทึกเวลาสุดท้ายที่ชนะ
                end_time = elapsed_time
            # แสดงข้อความ AI ชนะและจำนวนการเคลื่อนไหว
            win_text = font.render(f"AI Wins! Time: {int(end_time)}s", True, BLUE)
            final_moves_text = font.render(f"Moves: {move_count_ai}", True, BLUE)
            screen.blit(win_text, (900, SCREEN_HEIGHT - 100))
            screen.blit(final_moves_text, (900, SCREEN_HEIGHT - 50))   



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() # return position in the display x , y 
                print(pos)
                row, col = utils.get_clicked_cell(pos)

                # ตรวจสอบว่าคลิกอยู่ในแถวหรือคอลัมน์เดียวกับช่องว่างหรือไม่
                if row == empty_row and col != empty_col:  # คลิกในแถวเดียวกัน
                    utils.shift_row(row, empty_col, col, numbers_1)
                    empty_col = col
                elif col == empty_col and row != empty_row:  # คลิกในคอลัมน์เดียวกัน
                    utils.shift_col(col, empty_row, row, numbers_1)
                    empty_row = row
                    
                # if button_restart.is_clicked(event.pos):
                #     print("KONG restart or new shuwwsfel")
                    # # สร้างลิสต์ตัวเลข (สุ่มเฉพาะ 15 ตัวแรก)
                    # numbers = list(range(1, GRID_SIZE * GRID_SIZE))  # สร้างลิสต์ตั้งแต่ 0 ถึง 15 มีทั้งหมด 16 ตัว เเต่ เลือกเเค่ 1-15  
                    # print(numbers) #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

                    # random.shuffle(numbers)  # สุ่มลำดับตัวเลข
                    # print(numbers) #  random  มีจำนวน 15 ตัว เเละตัวสุดท้ายคือข้างล่าง
                    # numbers.append(0)  # เพิ่มช่องว่าง (0) ในตำแหน่งสุดท้าย
                    
                elif button_back.is_clicked(event.pos):
                    print("KONG back game page 1")
                    game1_running = False

        if not utils.check_win(numbers_1) and time.time() - last_move_time > 0.17:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ai_numbers = solution_path[move_index]
                move_index_player += 1
                move_count_player += 1  # นับจำนวนครั้งที่ AI เลื่อนตำแหน่ง
                last_move_time = time.time()
            # else:
            #     ai_won = True  # ตั้งค่าให้ AI ชนะเมื่อสิ้นสุดเส้นทาง

        if not ai_won and time.time() - last_move_time > 0.5:
            if move_index_ai < len(solution_path):
                numbers_2 = solution_path[move_index_ai]
                move_index_ai += 1
                move_count_ai += 1  # นับจำนวนครั้งที่ AI เลื่อนตำแหน่ง
                last_move_time = time.time()
            else:
                ai_won = True  # ตั้งค่าให้ AI ชนะเมื่อสิ้นสุดเส้นทาง
        
    
    
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    # return False









# not use now   ??????????????????????????
def gameAlgorithm_loop( numbers, screen ):
    print("algorithm is came in now!!! ")
    
    SCREEN_WIDTH = main.SCREEN_WIDTH 
    SCREEN_HEIGHT = main.SCREEN_HEIGHT 
    GRID_SIZE = main.GRID_SIZE 
    CELL_SIZE = main.CELL_SIZE - 15
    BACKGROUND_COLOR = main.BACKGROUND_COLOR  # Gray
    font = main.font
    ai_numbers = numbers
    

    clock = pygame.time.Clock()

    # สุ่มสถานะเริ่มต้นของกระดาน
    # while True:
    #     ai_numbers = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    #     random.shuffle(ai_numbers)
    #     if solver.is_solvable(ai_numbers):
    #         break

    goal_state = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    ai_won = False
    last_move_time = time.time()
    solution_path = solver.ida_star_search(ai_numbers, goal_state)
    move_index = 1  # เริ่มที่การเคลื่อนไหวครั้งแรก
    move_count = 0  # ตัวแปรสำหรับนับการเคลื่อนไหว
    end_time = None  # เก็บค่าเวลาที่เกมจบ

    # วาดกระดานเกมก่อนเพื่อแสดงผล
    screen.fill(GREY)
    solver.draw_grid(ai_numbers , screen)
    pygame.display.flip()
    
    # เริ่มจับเวลาหลังจากแสดงผลกระดานเกม
    start_time = time.time()

    running = True
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        screen.fill(GREY)
        solver.draw_grid(ai_numbers , screen)

        if not ai_won:
            # แสดงเวลาและจำนวนการเคลื่อนไหวแบบเรียลไทม์
            time_text = font.render(f"Time: {int(elapsed_time)}s", True, BLACK)
            moves_text = font.render(f"Moves: {move_count}", True, BLACK)
            screen.blit(time_text, (50, SCREEN_HEIGHT - 100))
            screen.blit(moves_text, (50, SCREEN_HEIGHT - 50))

        if ai_won:
            if end_time is None:  # ถ้าเกมเพิ่งจบ ให้บันทึกเวลาสุดท้ายที่ชนะ
                end_time = elapsed_time
            # แสดงข้อความ AI ชนะและจำนวนการเคลื่อนไหว
            win_text = font.render(f"AI Wins! Time: {int(end_time)}s", True, BLUE)
            final_moves_text = font.render(f"Moves: {move_count}", True, BLUE)
            screen.blit(win_text, (50, SCREEN_HEIGHT - 100))
            screen.blit(final_moves_text, (50, SCREEN_HEIGHT - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not ai_won and time.time() - last_move_time > 0.5:
            if move_index < len(solution_path):
                ai_numbers = solution_path[move_index]
                move_index += 1
                move_count += 1  # นับจำนวนครั้งที่ AI เลื่อนตำแหน่ง
                last_move_time = time.time()
            else:
                ai_won = True  # ตั้งค่าให้ AI ชนะเมื่อสิ้นสุดเส้นทาง

        pygame.display.flip()
        clock.tick(60)



# def get_clicked_cell(pos):  
#     x, y = pos 
#     col = ( x // CELL_SIZE )
#     row = ( y // CELL_SIZE )  
#     return row, col

# def shift_row(row, empty_col, clicked_col, numbers):
#     if clicked_col < empty_col:
#         # เลื่อนตัวเลขไปทางขวา
#         for col in range(empty_col, clicked_col, -1):
#             numbers[row * GRID_SIZE + col] = numbers[row * GRID_SIZE + (col - 1)]
#     else:
#         # เลื่อนตัวเลขไปทางซ้าย
#         for col in range(empty_col, clicked_col):
#             numbers[row * GRID_SIZE + col] = numbers[row * GRID_SIZE + (col + 1)]
#     numbers[row * GRID_SIZE + clicked_col] = 0  # ช่องว่างย้ายมาที่ตำแหน่งใหม่
    
# def shift_col(col, empty_row, clicked_row, numbers):
#     if clicked_row < empty_row:
#         # เลื่อนตัวเลขลง
#         for row in range(empty_row, clicked_row, -1):
#             numbers[row * GRID_SIZE + col] = numbers[(row - 1) * GRID_SIZE + col]
#     else:
#         # เลื่อนตัวเลขขึ้น
#         for row in range(empty_row, clicked_row):
#             numbers[row * GRID_SIZE + col] = numbers[(row + 1) * GRID_SIZE + col]
#     numbers[clicked_row * GRID_SIZE + col] = 0  # ช่องว่างย้ายมาที่ตำแหน่งใหม่
    
    
# def check_win(numbers):
#     return numbers == list(range(1, GRID_SIZE * GRID_SIZE)) + [0]






