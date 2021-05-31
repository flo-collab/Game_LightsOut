import numpy as np
import random
grid_size = 3

def generate_new_grid():
    new_grid = np.random.randint(0,2,size=(grid_size,grid_size))
    return new_grid


print(generate_new_grid())

def make_mat_clic(i,j):
    mat_clic = np.zeros((grid_size,grid_size))
    
    mat_clic[i,j] = 1

    if (i-1) >= 0:
        mat_clic[i-1,j]=1

    if (i+1)<= (grid_size-1):
        mat_clic[i+1,j]=1 
    
    if (j-1) >= 0:
        mat_clic[i,j-1]=1

    if (j+1) <= (grid_size-1):
        mat_clic[i,j+1]=1

    return (mat_clic,(i+1+j*grid_size))


print(make_mat_clic(2,1))


def play():
	pass





