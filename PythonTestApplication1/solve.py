# добавить несимметричность мира по горизонтали ивертикали
# сделать мир замкнутым по горизонтали

#import drawTurtle as tdraw
import drawPygame as tdraw
from settings import *

import time
from pygame import event, QUIT
#import turtle

# tree
#tree_turtle = []
tdraw.update()

min_side = (columns if columns <= rows else rows)
k=0
while (k < min_side):
    print(k)
    k += 1
    # redraw window
    tdraw.update()
    if (k < min_side):
        time.sleep(0.05) #0.05)
    tdraw.cornToTree()
    # update corn
    if (k != 1):
        corn = newCorn
    newCorn = []
    for cellCorn in corn:
        if (world[cellCorn[1]][cellCorn[2]] == 2):
            activeDNA = dna_start[cellCorn[0]]
            # right
            if ((activeDNA[0] < 16) & (world[cellCorn[1]][cellCorn[2]-1] == 0)):
                newCorn.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
                tree.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
                world[cellCorn[1]][cellCorn[2]-1] = 2
                #print("right")
                tdraw.addCorn(cellCorn[1],cellCorn[2]-1)

            # up
            if ((activeDNA[1] < 16) & (world[cellCorn[1]-1][cellCorn[2]] == 0)):
                newCorn.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
                tree.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
                world[cellCorn[1]-1][cellCorn[2]] = 2
                #print("up")
                tdraw.addCorn(cellCorn[1]-1,cellCorn[2])

            # left
            if ((activeDNA[2] < 16) & (world[cellCorn[1] ][cellCorn[2]+1] == 0)):
                newCorn.append([activeDNA[2], cellCorn[1], cellCorn[2]+1])
                tree.append([activeDNA[3], cellCorn[1], cellCorn[2]+1])
                world[cellCorn[1]][cellCorn[2]+1] = 2
                #print("left")
                tdraw.addCorn(cellCorn[1],cellCorn[2]+1)

            # down
            if ((activeDNA[3] < 16) & (world[cellCorn[1]+1][cellCorn[2]] == 0)):
                newCorn.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
                tree.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
                world[cellCorn[1]+1][cellCorn[2]] = 2
                #print("down")
                tdraw.addCorn(cellCorn[1]+1,cellCorn[2])

            world[cellCorn[1]][cellCorn[2]] = 1
tdraw.update()
# cycle for keep window after solve
flag = True
while flag:
    time.sleep(0.1)
    for ev in event.get():
        if ev.type == QUIT:
            flag = False