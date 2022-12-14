#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:16:03 2022

@author: podolnik
"""

import copy
import numpy as np

def l2p(l):
    l = l.strip().split(' -> ')
    path = []
    for e in l:
        e = e.split(',')
        path.append((int(e[1]), int(e[0])))
    return path
            
        
with open('input.txt', 'r') as f:
    rocks = [l2p(l) for l in f.readlines()]

# part 1

def get_next(field, loc, limit = None):
    if limit is not None:
        if loc[0] == limit + 1:
            return None
    
    test = (loc[0] + 1, loc[1])
    if not test in field:
        return test
    
    test = (loc[0] + 1, loc[1] - 1)
    if not test in field:
        return test
    
    test = (loc[0] + 1, loc[1] + 1)
    if not test in field:
        return test
    
    return None


field = {}    

for path in rocks:
    field[path[0]] = '#'
    for i in range(len(path) - 1):
        r0 = path[i]
        r1 = path[i + 1]
        dr = np.sign(r1[0] - r0[0])
        dc = np.sign(r1[1] - r0[1])
        ri = r0
        field[ri] = '#'
        while not ri == r1:
            ri = (ri[0] + dr, ri[1] + dc)
            field[ri] = '#'

max_r = max([k[0] for k in field])
origin = (0, 500)
field[origin] = '+'

def print_field(field):
    
    min_r = min([k[0] for k in field])
    min_c = min([k[1] for k in field])
    max_r = max([k[0] for k in field])
    max_c = max([k[1] for k in field])

    for r in range(min_r, max_r + 1):
        row = ''
        for c in range(min_c, max_c + 1):
            if (r, c) in field:
                row += field[(r, c)]
            else:
                row += '.'
        print(row)
        
grain_field = copy.deepcopy(field)
n_grains = 0
while True:
    grain = origin
    abbys = False
    while True:
        grain_next = get_next(grain_field, grain)
        if grain_next is None:
            grain_field[grain] = 'o'
            break
        elif grain_next[0] >= max_r:
            abbys = True
            break
        grain = grain_next
    if abbys:
        break        
    n_grains += 1
        
print(n_grains)
        
# part 2        
grain_field = copy.deepcopy(field)
n_grains = 0
while True:
    grain = origin
    filled = False
    while True:
        grain_next = get_next(grain_field, grain, limit = max_r)
        if grain_next is None and grain == origin:
            filled = True
            grain_field[grain] = 'o'
            n_grains += 1
            break
        elif grain_next is None:
            grain_field[grain] = 'o'
            break
        grain = grain_next
    if filled:
        break        
    n_grains += 1
        
print(n_grains)
