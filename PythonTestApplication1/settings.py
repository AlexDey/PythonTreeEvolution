from random import randint, seed

# start DNA
seed(38) #30 #9 #34 #38
dna_start = [[randint(0,30) for i in range(4)] for j in range(16)] 

# start data for solve
#rows = columns = 40
rows = 60
columns = 40
row_start = rows #*2-2  # *7//4
column_start = columns
world = [[(0) for i in range(columns*2)] for j in range(rows*2)] # start world
world[row_start][column_start] = 2 # start corn
world[-1][:] = [3]*columns*2 # ground
corn = [[0, row_start, column_start]]
tree = corn.copy() # copy;  # tree = corn - just reference
newCorn = []
