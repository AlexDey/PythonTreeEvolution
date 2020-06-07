# залить изменения на gitlab
# сделать систему отрисовки через pygame

import drawTurtle as tdraw
from drawTurtle import corn_turtle
from settings import *

import time
import turtle

# tree
#tree_turtle = []
tdraw.update()
   
#global corn_turtle
k=0
while (k < rows-1):
    print(k)
    k += 1
    # redraw window with turtle
    tdraw.update()
    if (k < rows/2):
        time.sleep(0.1)
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

                tdraw.addCorn(cellCorn[1],cellCorn[2]-1)

            # up
            if ((activeDNA[1] < 16) & (world[cellCorn[1]-1][cellCorn[2]] == 0)):
                newCorn.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
                tree.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
                world[cellCorn[1]-1][cellCorn[2]] = 2

                tdraw.addCorn(cellCorn[1]-1,cellCorn[2])

            # left
            if ((activeDNA[2] < 16) & (world[cellCorn[1] ][cellCorn[2]+1] == 0)):
                newCorn.append([activeDNA[2], cellCorn[1], cellCorn[2]+1])
                tree.append([activeDNA[3], cellCorn[1], cellCorn[2]+1])
                world[cellCorn[1]][cellCorn[2]+1] = 2

                tdraw.addCorn(cellCorn[1],cellCorn[2]+1)

            # down
            if ((activeDNA[3] < 16) & (world[cellCorn[1]+1][cellCorn[2]] == 0)):
                newCorn.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
                tree.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
                world[cellCorn[1]+1][cellCorn[2]] = 2

                tdraw.addCorn(cellCorn[1]+1,cellCorn[2])

            world[cellCorn[1]][cellCorn[2]] = 1