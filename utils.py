# import threading
# import pygame
# from sys import exit
# import sys
import random
# import time

# from ui import Button , Grid , DynamicSizeObject
# import game
import main

# GRID_SIZE = main.getGrid_size
# main.CELL_SIZE = main.getCell_size

class ListNumber():
    def __init__ (self , GRID_SIZE):
        self.GRID_SIZE =  GRID_SIZE

    def randomNumber(self):
         # สร้างลิสต์ตัวเลข (สุ่มเฉพาะ 15 ตัวแรก)
        numbers = list(range(1, self.GRID_SIZE * self.GRID_SIZE))  # สร้างลิสต์ตั้งแต่ 0 ถึง 15 มีทั้งหมด 16 ตัว เเต่ เลือกเเค่ 1-15  
        print(numbers) #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        random.shuffle(numbers)  # สุ่มลำดับตัวเลข
        print(numbers) #  random  มีจำนวน 15 ตัว เเละตัวสุดท้ายคือข้างล่าง
        numbers.append(0)  # เพิ่มช่องว่าง (0) ในตำแหน่งสุดท้าย
        
        return numbers
    
    #                   list to check 
    def is_solvable(self , numbers):
        inversions = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] and numbers[j] and numbers[i] > numbers[j]:
                    inversions += 1
        zero_row = numbers.index(0) // self.GRID_SIZE
        if self.GRID_SIZE % 2 == 1:
            return inversions % 2 == 0
        else:
            return (inversions + zero_row) % 2 == 1
        
        


def get_clicked_cell(pos):  
    x, y = pos 
    col = ( x // main.CELL_SIZE )
    row = ( y // main.CELL_SIZE )  
    return row, col

def shift_row(row, empty_col, clicked_col, numbers):
    if clicked_col < empty_col:
        # เลื่อนตัวเลขไปทางขวา
        for col in range(empty_col, clicked_col, -1):
            numbers[row * main.GRID_SIZE + col] = numbers[row * main.GRID_SIZE + (col - 1)]
    else:
        # เลื่อนตัวเลขไปทางซ้าย
        for col in range(empty_col, clicked_col):
            numbers[row * main.GRID_SIZE + col] = numbers[row * main.GRID_SIZE + (col + 1)]
    numbers[row * main.GRID_SIZE + clicked_col] = 0  # ช่องว่างย้ายมาที่ตำแหน่งใหม่
    
def shift_col(col, empty_row, clicked_row, numbers):
    if clicked_row < empty_row:
        # เลื่อนตัวเลขลง
        for row in range(empty_row, clicked_row, -1):
            numbers[row * main.GRID_SIZE + col] = numbers[(row - 1) * main.GRID_SIZE + col]
    else:
        # เลื่อนตัวเลขขึ้น
        for row in range(empty_row, clicked_row):
            numbers[row * main.GRID_SIZE + col] = numbers[(row + 1) * main.GRID_SIZE + col]
    numbers[clicked_row * main.GRID_SIZE + col] = 0  # ช่องว่างย้ายมาที่ตำแหน่งใหม่
    
    
def check_win(numbers):
    return numbers == list(range(1, main.GRID_SIZE * main.GRID_SIZE)) + [0]