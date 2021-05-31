import numpy as np
import random

def generate_new_grid(grid_size):
    new_grid = np.random.randint(0,2,size=(grid_size,grid_size))
    return new_grid


print(generate_new_grid(5))



def play():
	pass
