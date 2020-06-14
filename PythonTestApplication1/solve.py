# дать дереву энергию, которая тратиться каждый ход на поддержание жизни клетки
# Сделать энергию солнца которая разная в зависимости от высоты 
# сделать чтоб клетки поглащало энергию

#import drawTurtle as tdraw
import drawPygame as tdraw
from settings import *

from time import sleep
from pygame import event, QUIT, KEYUP, K_p
#import turtle

def pause_pygame():
    """pause pygame work, for pause/unpause use 'p' """
    global pause
    for ev in event.get():
        if ev.type == KEYUP:
            if ev.key == K_p:
                pause = True
    while pause:
        for ev in event.get():
            if ev.type == KEYUP:
                if ev.key == K_p:
                    pause = False

def grow_left():
    if (cellCorn[2] == 0):
        cellCorn[2] = (columns)
    if ((activeDNA[0] < 16) & (world[cellCorn[1]][cellCorn[2]-1] == 0)):
        newCorn.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
        tree.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
        world[cellCorn[1]][cellCorn[2]-1] = 2
        tdraw.addCorn(cellCorn[1],cellCorn[2]-1)
    if (cellCorn[2] == (columns)):
        cellCorn[2] = 0

def grow_right():
    if (cellCorn[2] == (columns-1)):
        cellCorn[2] = -1
    if ((activeDNA[2] < 16) & (world[cellCorn[1]][cellCorn[2]+1] == 0)):
        newCorn.append([activeDNA[2], cellCorn[1], cellCorn[2]+1])
        tree.append([activeDNA[3], cellCorn[1], cellCorn[2]+1])
        world[cellCorn[1]][cellCorn[2]+1] = 2
        tdraw.addCorn(cellCorn[1],cellCorn[2]+1)
    if (cellCorn[2] == -1):
        cellCorn[2] = (columns-1)

def grow_up():
    if ((activeDNA[1] < 16) & (world[cellCorn[1]-1][cellCorn[2]] == 0)):
        newCorn.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
        tree.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
        world[cellCorn[1]-1][cellCorn[2]] = 2
        tdraw.addCorn(cellCorn[1]-1,cellCorn[2])

def grow_down():
    if ((activeDNA[3] < 16) & (world[cellCorn[1]+1][cellCorn[2]] == 0)):
        newCorn.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
        tree.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
        world[cellCorn[1]+1][cellCorn[2]] = 2
        tdraw.addCorn(cellCorn[1]+1,cellCorn[2])

# def main():
# tree
#tree_turtle = []
tdraw.update()
min_side = 365# (columns if columns <= rows else rows)
k=0
while (k < min_side):
    print(k)
    k += 1

    # redraw window
    tdraw.update()
    tdraw.cornToTree()

    #pause
    #if (k > 180):
    #   pause_pygame()
    pause_pygame()

    # timestep
    if (k < min_side):
       sleep(0.005)

    # update corn
    if (k != 1):
        corn = newCorn
    newCorn = []
    for cellCorn in corn:
        if (world[cellCorn[1]][cellCorn[2]] == 2):
            activeDNA = dna_start[cellCorn[0]]

            grow_left()
            grow_up()
            grow_right()
            grow_down()

            world[cellCorn[1]][cellCorn[2]] = 1
tdraw.update()
# cycle for keep window after solve
flag = True
while flag:
    sleep(0.25)
    try:
        for ev in event.get():
            if ev.type == QUIT:
                sys.exit()
                pygame.quit()
                #flag = False
    except BaseException:
        flag = False

# main()