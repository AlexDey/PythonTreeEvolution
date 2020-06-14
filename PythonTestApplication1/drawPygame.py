# здесь будет сделана система отрисовки через pygame, 
# сначала нужно инициализировать экран и первое зёрнышко по общим данным из settings,
# затем добавить функции отрисовки вновь появившихся семок и обновившихся древоклеток
import pygame
import os
#import ctypes
#from ctypes import windll #.user32.GetSystemMetrics

from settings import rows, columns, row_start, column_start

def addCorn(row, column):
    x_pos = column*rect_size
    y_pos = row*rect_size
    corn_new = pygame.draw.rect(win, color_corn, (x_pos, y_pos, rect_size, rect_size))
    corn_turtle.append(corn_new)

def update():
    pygame.display.update(tree_new)
    pygame.display.update(corn_turtle)


def cornToTree():
    """fill corn like tree and clear 'corn_turtle' matrix"""
    tree_new[:] = []
    for corn_one in corn_turtle:
        tree_one_new = pygame.draw.rect(win, color_tree, corn_one)
        tree_new.append(tree_one_new)
    corn_turtle[:] = []

# start data for draw window with pygame
#scale = .4
constant_size = 24 # 24 # = rows * scale
scale_rows = constant_size / rows*2 #(columns if columns <= rows else rows) #columns
rect_size = 21 * scale_rows # 21 is standart size rect for turtle
width = rect_size*columns
height = rect_size*rows

# resize if width > window resolution
pygame.init()
width_screen = pygame.display.Info().current_w
#height_screen = pygame.display.Info().current_h
if width > width_screen:
    ratio_wh = 1.89 # experimental value , width_screen/height_screen = 1.7777
    scale_columns = constant_size*ratio_wh / columns*2
    rect_size = 21 * scale_columns
    width = rect_size*columns
    height = rect_size*rows


# set window position
startx = pygame.display.Info().current_w-width-5
starty = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (startx, starty)
# window
win = pygame.display.set_mode((int(width), int(height)))

# first corn
corn_turtle = []
x_pos_start = column_start*rect_size
y_pos_start = row_start*rect_size
color_corn = (255,255,255)
corn_start = pygame.draw.rect(win, color_corn, (x_pos_start, y_pos_start, rect_size, rect_size))
corn_turtle.append(corn_start)

# tree
color_tree = (0,255,0)
tree_new = []

# ground
x_ground = 0
y_ground = (rows-1)*rect_size
color_ground = (125, 0, 0)
ground = pygame.draw.rect(win, color_ground, (x_ground, y_ground, rect_size*columns, rect_size))
pygame.display.update(ground)

# close window by key
#fps = 5
#clock = pygame.time.Clock()
#flag = True
#while flag:
#    clock.tick(fps)
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            flag = False
#            #pygame.quit()
#        elif event.type == pygame.MOUSEBUTTONUP:
#            cornToTree()
    #pygame.display.update()