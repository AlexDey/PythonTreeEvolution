from random import randint, seed

# start DNA
seed(31) #30 #9 #555
dna_start = [[randint(0,30) for i in range(4)] for j in range(16)] 

# start data for solve
#rows = 60
#columns = 60
rows = columns = 80
world = [[(0) for i in range(rows*2)] for j in range(columns*2)] # start world
world[rows][columns] = 2
tree = [[0, rows, columns]]
corn = [[0, rows, columns]]
newCorn = []

# start data for draw window with turtle
#scale = .4
#rect_size = 21 * scale
#width = rect_size*rows*2
#height = rect_size*columns*2

# turtle temp
#corn_turtle = []