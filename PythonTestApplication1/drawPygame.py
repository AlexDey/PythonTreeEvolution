# здесь будет сделана система отрисовки через pygame, 
# сначала нужно инициализировать экран и первое зёрнышко по общим данным из settings,
# затем добавить функции отрисовки вновь появившихся семок и обновившихся древоклеток
import pygame
import os

from settings import rows, columns

def addCorn(row, column):
    x_pos = column*rect_size
    y_pos = row*rect_size
    corn_new = pygame.draw.rect(win, color_corn, (x_pos, y_pos, rect_size, rect_size))
    corn_turtle.append(corn_new)

def update():
    pygame.display.update(corn_turtle)


def cornToTree():
    """fill corn like tree and clear 'corn_turtle' matrix"""
    tree_new = []
    for corn_one in corn_turtle:
        tree_one_new = pygame.draw.rect(win, color_tree, corn_one)
        tree_new.append(tree_one_new)
    pygame.display.update(tree_new)
    corn_turtle[:] = []

# start data for draw window with pygame
#scale = .4
constant_size = 24 # = rows * scale
scale = constant_size / columns
rect_size = 21 * scale
width = rect_size*rows*2
height = rect_size*columns*2

# set window position
pygame.init()
startx = pygame.display.Info().current_w-width-5
starty = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (startx, starty)
# window
win = pygame.display.set_mode((int(width), int(height)))

# first corn
corn_turtle = []
x_pos_start = columns*rect_size
y_pos_start = rows*rect_size
color_corn = (255,255,255)
corn_start = pygame.draw.rect(win, color_corn, (x_pos_start, y_pos_start, rect_size, rect_size))
corn_turtle.append(corn_start)

# tree
color_tree = (0,255,0)

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