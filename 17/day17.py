#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:00:13 2022

@author: podolnik
"""

with open('input.txt', 'r') as f:
    jet = list(f.read().strip())

# part 1

rock_a = [[1, 1, 1, 1]]
rock_b = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
rock_c = [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
rock_d = [[1], [1], [1], [1]]
rock_e = [[1, 1], [1, 1]]

dirs = {'>': (0, 1), '<': (0, -1)}
field_w = 7

def r2s(rock):
    rock_set = set()
    for r in range(len(rock)):
        for c in range(len(rock[r])):
            if rock[r][c] == 1:                
                rock_set.add((r, c))
    return rock_set
                

rocks = [r2s(rock) for rock in [rock_a, rock_b, rock_c, rock_d, rock_e]]
rock_sizes = [(len(rock), len(rock[0])) for rock in [rock_a, rock_b, rock_c, rock_d, rock_e]]


def can_move(rock, field, dr = 0, dc = 0):
    for stone in rock:
        if stone[1] + dc < 0 or stone[1] + dc >= field_w:
            return False
        if (stone[0] + dr, stone[1] + dc) in field:
            return False
    return True

def move(stones, dr = 0, dc = 0):
    return set([(s[0] + dr, s[1] + dc) for s in stones])  

def print_field(field, rock = None):
    r_min = min([s[0] for s in field])
    r_max = max([s[0] for s in field])
    c_min = min([s[1] for s in field])
    c_max = max([s[1] for s in field])
    
    if rock:
        r_min = min([s[0] for s in rock])
    
    for r in range(r_min, r_max + 1):
        row = '{:04d} |'.format(r)
        for c in range(c_min, c_max + 1):
            
            if rock is not None and (r, c) in rock:
                row += 'O'
            elif (r, c) in field:
                row += '#'
            else:
                row += ' '
        row += '|'
        print(row)
        
def restrict(field, h_max):
    result = set()
    r_min = min([s[0] for s in field])
    for s in field:
        if abs(s[0] - r_min) < h_max:
            result.add(s)
    return result    
        
def fill_field(num_rocks, find_repeat = False):
    field = set([(0, c) for c in range(7)])
    j = 0
    
    h = 0
    for i in range(num_rocks):
        ri = i % len(rocks)
        rock = rocks[ri]
        rock = move(rock, dr = -rock_sizes[ri][0] - 3 - h, dc = 2)    
        
        while True:
            dr, dc = dirs[jet[j]]
            
            if (j % len(jet) == 0) and ri == 0 and find_repeat and i > 0:
                return h, field, i
                
            j = (j + 1) % len(jet)
            
            if can_move(rock, field, dr=dr, dc=dc):
                rock = move(rock, dr=dr, dc=dc)
            if can_move(rock, field, dr = 1):
                rock = move(rock, dr=1)
            else:
                for s in rock:
                    h = max(h, abs(s[0]))
                    field.add(s)
                break   
            
        field = restrict(field, 50)
        if i % 10000 == 0:
            print(i)
    return h, field, i

h, field, _ = fill_field(2022)
print(h)

# part 2

h, field, _ = fill_field(100000000, find_repeat=True)
print(h)

print_field(field)