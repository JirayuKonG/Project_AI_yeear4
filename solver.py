import pygame
from sys import exit
from ui import Button , Grid , DynamicSizeObject

import main
# import game
# import ui
# import utils
    

def getGoalStage():
    goal_state = list(range(1, main.GRID_SIZE * main.GRID_SIZE)) + [0]
    return goal_state


def ai_move(numbers, goal_state):
    solution_path = ida_star_search(numbers, goal_state)
    if solution_path and len(solution_path) > 1:
        return solution_path[1] 
    return None


def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:
            current_row, current_col = i // main.GRID_SIZE, i % main.GRID_SIZE
            goal_row, goal_col = (state[i] - 1) // main.GRID_SIZE, (state[i] - 1) % main.GRID_SIZE
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def ida_star_search(start_state, goal_state):
    def dfs(path, g, threshold):
        node = path[-1]
        f = g + manhattan_distance(node, goal_state)
        if f > threshold:
            return f
        if node == goal_state:
            return 'FOUND'
        min_threshold = float('inf')
        empty_index = node.index(0)
        empty_row, empty_col = empty_index // main.GRID_SIZE, empty_index % main.GRID_SIZE
        possible_moves = []  # create list 
        if empty_row > 0:
            possible_moves.append((empty_row - 1, empty_col))  # Move Up
        if empty_row < main.GRID_SIZE - 1:
            possible_moves.append((empty_row + 1, empty_col))  # Move Down
        if empty_col > 0:
            possible_moves.append((empty_row, empty_col - 1))  # Move Left
        if empty_col < main.GRID_SIZE - 1:
            possible_moves.append((empty_row, empty_col + 1))  # Move Right
        for new_row, new_col in possible_moves:
            new_index = new_row * main.GRID_SIZE + new_col
            new_state = node[:]
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            if new_state not in path:
                path.append(new_state)
                t = dfs(path, g + 1, threshold)
                if t == 'FOUND':
                    return 'FOUND'
                if t < min_threshold:
                    min_threshold = t
                path.pop()
        return min_threshold

    threshold = manhattan_distance(start_state, goal_state)   # find distance between node
    path = [start_state] # create a list 
    while True:
        t = dfs(path, 0, threshold)
        if t == 'FOUND':
            return path
        if t == float('inf'):
            return None  # ไม่พบเส้นทาง
        threshold = t
        
        
def draw_grid(numbers , screen):
    for row in range(main.GRID_SIZE):
        for col in range(main.GRID_SIZE):
            num = numbers[row * main.GRID_SIZE + col]
            rect = pygame.Rect(col * main.CELL_SIZE, row * main.CELL_SIZE, main.CELL_SIZE, main.CELL_SIZE)
            pygame.draw.rect(screen, main.WHITE, rect)
            pygame.draw.rect(screen, main.BLACK, rect, 2)

            if num != 0:  # 0 แทนช่องว่าง
                text = main.font.render(str(num), True, main.BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)