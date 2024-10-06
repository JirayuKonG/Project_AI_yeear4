import pygame


# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)

    
# Button class
class Button:
    def __init__(self, x, y, width, height, text):  # like a constructure  ==>   Button( x, y, width, height, text )
        self.rect = pygame.Rect(x, y, width, height) # self like a create a  variable in class    draw a regtangle
        self.text = text  # the variable name is "text"
        self.color = LIGHT_BLUE # the variable name is "color"

    def draw(self, screen):
        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)  # Border
        
        # Render the text on the button
        font = pygame.font.Font(None, 40)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect) # นี่จะวาดข้อความลงบนหน้าจอที่ตำแหน่งที่กำหนด

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)  # เพื่อตรวจสอบว่าจุด (ตำแหน่งคลิกเมาส์) อยู่ภายในสี่เหลี่ยมของปุ่มหรือไม่ ซึ่งจะคืนค่า True ถ้าปุ่มถูกคลิกและ False ถ้าไม่
    
class Grid():
    def __init__(self, grid_size, cell_size, x, y ):
        # self.rect = pygame.Rect(x, y, width, height)    # self like a create a  variable in class    draw a regtangle
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.x = x   # start display x
        self.y = y   # start display y
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen, numbers):
        
         for row in range(self.grid_size):
            for col in range(self.grid_size):
                num = numbers[row * self.grid_size + col]
                #                       position x                         position y                     width                height 
                rect = pygame.Rect( (col * self.cell_size) + self.x , (row * self.cell_size) + self.y , self.cell_size , self.cell_size )
        
                # วาดสี่เหลี่ยมสำหรับแต่ละเซลล์
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 3)  # Border
        
                if num != 0 :   # 0 แทนช่องว่าง วาด text ตัวเลขใน grid  
                    # Render the text on the button
                    text_surface = self.font.render(str(num), True, BLACK)
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect) # นี่จะวาดข้อความลงบนหน้าจอที่ตำแหน่งที่กำหนด


class DynamicSizeObject():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def draw_dynamic( self ):  # only regtagle (4 มุม)
        # Calculate dynamic size and position based on the screen size
        square_size = int(self.screen_width * 0.1)  # 10% of screen width
        
        square_x = int(self.screen_width * 0.45)  # 45% from the left of the screen
        square_y = int(self.screen_height * 0.4)  # 40% from the top of the screen

        # Draw a square
        # square_rect = pygame.Rect(square_x, square_y, square_size, square_size) 
        # pygame.draw.rect(screen, BLUE, square_rect)
        
        button_start1 = Button( (square_x / 2) -230 , square_y / 4 , 600-square_size , 80-square_size , "Start Game 1st")
        button_start2 = Button( (square_x / 2) -230 , square_y / 2.5, 600, 80, "Start Game 1st Vs Bot using ai algorithm")
        button_quit = Button( (square_x / 2) -230 , square_y / 1.75 , 600, 80, "Quit Game")
        
        return button_start1 , button_start2 , button_quit
        
    
    