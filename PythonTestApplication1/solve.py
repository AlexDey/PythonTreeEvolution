# дать дереву энергию, которая тратиться каждый ход на поддержание жизни клетки ++
# Сделать энергию солнца которая разная в зависимости от высоты ++
# сделать чтоб клетки поглащало энергию ++
# дерево поглащают энергию отдельно, зерно отдельно

#import drawTurtle as tdraw
import drawPygame as tdraw
from settings import *

from time import sleep
from pygame import event, QUIT, KEYUP, K_p


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
        cellCorn[2] = columns
    if ((activeDNA[0] < 16) & (world[cellCorn[1]][cellCorn[2]-1] == 0)):
        newCorn.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
        tree.append([activeDNA[0], cellCorn[1], cellCorn[2]-1])
        world[cellCorn[1]][cellCorn[2]-1] = 2
        tdraw.addCorn(cellCorn[1],cellCorn[2]-1)
        energy_corn_decrease("left")
    if (cellCorn[2] == columns):
        cellCorn[2] = 0

def grow_right():
    if (cellCorn[2] == columns-1):
        cellCorn[2] = -1
    if ((activeDNA[2] < 16) & (world[cellCorn[1]][cellCorn[2]+1] == 0)):
        newCorn.append([activeDNA[2], cellCorn[1], cellCorn[2]+1])
        tree.append([activeDNA[3], cellCorn[1], cellCorn[2]+1])
        world[cellCorn[1]][cellCorn[2]+1] = 2
        tdraw.addCorn(cellCorn[1],cellCorn[2]+1)
        energy_corn_decrease("right")
    if (cellCorn[2] == -1):
        cellCorn[2] = columns-1

def grow_up():
    if ((activeDNA[1] < 16) & (world[cellCorn[1]-1][cellCorn[2]] == 0)):
        newCorn.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
        tree.append([activeDNA[1], cellCorn[1]-1, cellCorn[2]])
        world[cellCorn[1]-1][cellCorn[2]] = 2
        tdraw.addCorn(cellCorn[1]-1,cellCorn[2])
        energy_corn_decrease("up")

def grow_down():
    if ((activeDNA[3] < 16) & (world[cellCorn[1]+1][cellCorn[2]] == 0)):
        newCorn.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
        tree.append([activeDNA[3], cellCorn[1]+1, cellCorn[2]])
        world[cellCorn[1]+1][cellCorn[2]] = 2
        tdraw.addCorn(cellCorn[1]+1,cellCorn[2])
        energy_corn_decrease("down")

def energy_corn_decrease(msg):
    global energy, energy_corn_grow
    energy -= energy_corn_grow
    print("-----------")
    print(msg)
    print("subtraction: ", -energy_corn_grow)
    print("all energy:  ", energy)

def energy_tree_decrease():
    global energy, k
    count_tree_cells = len(tree) - len(newCorn)
    energy_decrese = -energy_tree_live * count_tree_cells
    energy += energy_decrese
    print("===========")
    print("iter: ", k)
    print("tree sells:  ", count_tree_cells)
    print("decrease: ", energy_decrese)
    print("all energy:  ", energy)

def energy_increase():
    global energy
    tree_sort = sorted(sorted(tree, key=lambda tree: tree[1]), key=lambda tree: tree[2])
    column_local = -1 #tree_sort[0][2]
    multiplier = 3
    energy_increase = 0
    for tree_cell in tree_sort:
        if (tree_cell[2]!=column_local):
            column_local = tree_cell[2]
            multiplier = 3
            energy_increase += energy_sun_levels[tree_cell[1]] * multiplier
        elif (tree_cell[2]==column_local and multiplier > 1):
            multiplier -= 1
            energy_increase += energy_sun_levels[tree_cell[1]] * multiplier
    energy += energy_increase
    print("increase: ", energy_increase)
    print("all energy:  ", energy)

# def main():
# tree
#tree_turtle = []
tdraw.update()
min_side = 365# (columns if columns <= rows else rows)
k=0
while (k < min_side):
    k += 1
    # redraw window
    tdraw.update()
    tdraw.cornToTree()

    #pause
    #if (k > 180):
    #   pause_pygame()
    pause_pygame()

    energy_tree_decrease()
    energy_increase()

    # timestep
    if (k < min_side):
       sleep(1.005)

    # update corn
    corn = newCorn
    newCorn = []
    for cellCorn in corn:
        if (world[cellCorn[1]][cellCorn[2]] == 2):
            activeDNA = dna_start[cellCorn[0]]

            grow_up()
            grow_left()
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