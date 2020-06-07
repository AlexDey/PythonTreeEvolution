import time
import numpy as np
import matplotlib.pyplot as plt
from random import randint, seed

np.random.seed(15) #4 #69 #555
Z = np.random.randint(0,30, size=(16,4)) # start DNA

# start data
x = 80
y = 80
world = np.zeros((x*2, y*2), dtype=int)
world[x,y] = 2
tree = [[0, x, y]]
corn = [[0, x, y]]
newCorn = []

fig, ax = plt.subplots()
mng = plt.get_current_fig_manager()
mng.window.state('zoomed') # this is Screen Size
#fig.set_size_inches(18.5, 10.5)
ax.imshow(world, cmap='magma')
    
k=0
while (k < x-1):
    print(k)
    k += 1
    if (k%5 == 0):
        ax.imshow(world, cmap='magma')
        plt.draw()
        plt.pause(1e-17)
        #time.sleep(0.1)
    if (k != 1):
        corn = newCorn
    newCorn = []
    for cellCorn in corn:
        if (world[cellCorn[1],cellCorn[2]] == 2):
            activeDNA = Z[cellCorn[0]]
            if ((activeDNA[0] < 16) & (world[cellCorn[1]-1,cellCorn[2]] == 0)):
                newCorn.append([activeDNA[0], cellCorn[1]-1, cellCorn[2]])
                tree.append([activeDNA[0], cellCorn[1]-1, cellCorn[2]])
                world[cellCorn[1]-1,cellCorn[2]] = 2

            if ((activeDNA[1] < 16) & (world[cellCorn[1] ,cellCorn[2]+1] == 0)):
                newCorn.append([activeDNA[1], cellCorn[1], cellCorn[2]+1])
                tree.append([activeDNA[1], cellCorn[1], cellCorn[2]+1])
                world[cellCorn[1] ,cellCorn[2]+1] = 2

            if ((activeDNA[2] < 16) & (world[cellCorn[1]+1,cellCorn[2]] == 0)):
                newCorn.append([activeDNA[2], cellCorn[1]+1, cellCorn[2]])
                tree.append([activeDNA[2], cellCorn[1]+1, cellCorn[2]])
                world[cellCorn[1]+1,cellCorn[2]] = 2

            if ((activeDNA[3] < 16) & (world[cellCorn[1],cellCorn[2]-1] == 0)):
                newCorn.append([activeDNA[3], cellCorn[1], cellCorn[2]-1])
                tree.append([activeDNA[3], cellCorn[1], cellCorn[2]-1])
                world[cellCorn[1],cellCorn[2]-1] = 2

            world[cellCorn[1],cellCorn[2]] = 1
plt.show()