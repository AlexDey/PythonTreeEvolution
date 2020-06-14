from random import randint, seed

# start DNA
seed(70) #9 #30 #34 #38 #70
dna_start = [[randint(0,30) for i in range(4)] for j in range(16)] 

# example DNA from foo52
#dna_start = [[14, 13, 12, 30],  # 0
#             [30, 30, 30, 30],  # 1
#             [30, 30,  2,  9],  # 2
#             [30, 30, 30, 30],  # 3
#             [30, 30, 30, 30],  # 4
#             [30, 30, 30, 30],  # 5
#             [30, 30, 30, 30],  # 6
#             [30, 30, 30, 11],  # 7
#             [30, 15, 30, 30],  # 8
#             [30, 30,  0, 30],  # 9
#             [30, 30, 30, 30],  # 10
#             [ 8,  6,  2, 30],  # 11
#             [30, 30, 30,  7],  # 12
#             [30,  8, 30, 30],  # 13
#             [30, 30, 30, 30],  # 14
#             [30, 30,  9, 30],  # 15
#             ]

# start data for solve
#rows = columns = 40
rows = 100 # определяет высоту
columns = 256 # определяет ширина
row_start = rows-2  # on ground
column_start = columns//2 # center

world = [[(0) for i in range(columns)] for j in range(rows)] # start world
world[row_start][column_start] = 2 # start corn
world[-1][:] = [3]*columns # ground

corn = [[0, row_start, column_start]] # corn start position
tree = corn.copy() # copy;  # tree = corn - just reference
newCorn = [] # list for new iteration

energy = 300

# debug data
pause = False