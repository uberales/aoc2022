#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:30:12 2022

@author: podolnik
"""

import numpy as np

with open('input.txt', 'r') as f:
    grid = np.array([list(l.strip()) for l in f.readlines()])
    
# part 1
def get_letter(grid, letter):
    idx = np.where(grid == letter)
    return list(zip(*idx))

coord_S = get_letter(grid, 'S')[0]
coord_E = get_letter(grid, 'E')[0]

grid[coord_S] = 'a'
grid[coord_E] = 'z'
            
def get_next(grid, coords):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nr = len(grid)
    nc = len(grid[0])
    res = []
    
    ref = grid[coords]
    
    for d in dirs:
        c = (coords[0] + d[0], coords[1] + d[1])
        if c[0] >= 0 and c[1] >= 0 and c[0] < nr and c[1] < nc:
            comp = grid[c]
            if ord(ref) + 1 == ord(comp) or ord(ref) >= ord(comp):
                res.append(c)
    return res

def shortest(grid, start, end):
    
    dist_grid = np.empty(np.shape(grid), dtype=int)
    dist_grid[:] = -1
    dist_grid[start] = 0
    
    queue = [start]
    
    while len(queue) > 0:
        coords = queue.pop(0)
        neighbors = get_next(grid, coords)
        for n in neighbors:
            min_l = dist_grid[n]
            if min_l < 0 or min_l > dist_grid[coords] + 1:
                dist_grid[n] = dist_grid[coords] + 1
                queue.append(n)
                
    return dist_grid[end]
        
print(shortest(grid, coord_S, coord_E))
  
# part 2

coord_a = get_letter(grid, 'a')
dist_a = [shortest(grid, c, coord_E) for c in coord_a]

print(min([d for d in dist_a if d > 0]))