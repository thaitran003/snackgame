import pygame 
from sys import exit
from os.path import join

# khai báo các biến 
CELL_SIZE = 80  #kichs thươc ô 
ROWS = 10
COLS = 16
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

# khai báo biến màu
LIGHT_GREEN = '#aad751'
DARK_GREEN  = '#a2d149'

# khai bài vị trí và độ dài bắt đầu 
START_LENGTH = 3
START_ROW = ROWS // 2
START_COL = START_LENGTH + 2

# đổ bóng cho vật thể
SHADOW_SIZE = pygame.Vector2(4,4)
SHADOW_OPACITY = 100