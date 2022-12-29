#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:30:10 2022

@author: podolnik
"""

import copy

with open('input.txt', 'r') as f:
    field = [list(l.strip()) for l in f.readlines()]

# part 1
 
elves = set()

for r in range(len(field)):
    for c in range(len(field[r])):
        if field[r][c] == '#':
            elves.add((r, c))

dir_8 = [(ns, ew) for ns in (-1, 0, 1) for ew in (-1, 0, 1)  if (ns, ew) != (0, 0) ]
name_8 = [ns + ew for ns in ('N', '', 'S') for ew in ('W', '', 'E')  if len(ns + ew) > 0]
directions = dict(zip(name_8, dir_8))

init_conditions = [
    (('N', 'NE', 'NW'), 'N'),
    (('S', 'SE', 'SW'), 'S'),
    (('W', 'NW', 'SW'), 'W'),
    (('E', 'NE', 'SE'), 'E'),
    ]

def get_bounds(elves):
    r = [e[0] for e in elves]
    c = [e[1] for e in elves]
    return min(r), max(r), min(c), max(c)

def print_elves(elves):
    r_min, r_max, c_min, c_max = get_bounds(elves)
    
    for r in range(r_min - 1, r_max + 2):
        row = ''
        for c in range(c_min - 1, c_max + 2):
            if (r, c) in elves:
                row += '#'
            else:
                row += '.'
        print(row)
    print()

def add(pos, d):
    return (pos[0] + d[0], pos[1] + d[1])

def count_neighbors(elf, dir_names, elves):
    n_nbs = 0
    for dn in dir_names:
        d = directions[dn]
        pos = add(elf, d)
        if pos in elves:
            n_nbs += 1
    return n_nbs

def add_or_append(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]
    
def move(elves, init_conditions, n_rounds = None):        
    condition_def = init_conditions
    r = 0
    while True:
        candidates = {}
        for elf in elves:        
            total_nbs = count_neighbors(elf, name_8, elves)
            if total_nbs > 0:
                dir_found = False
                for condition, result in condition_def:
                    n_nbs = count_neighbors(elf, condition, elves)
                                            
                    if n_nbs == 0:
                        dir_found = True
                        d = directions[result]
                        pos = add(elf, d)
                        add_or_append(candidates, pos, elf)
                        break
                if not dir_found:
                    add_or_append(candidates, elf, elf)
            else:
                add_or_append(candidates, elf, elf)
                
        new_elves = set()
        for pos in candidates:
            moved = set()
            if len(candidates[pos]) == 1:
                moved.add(pos)
            else:
                moved = moved.union(candidates[pos])
                
            for e in moved:
                new_elves.add(e)
    
                
        r += 1
        if elves == new_elves:
            break
        else:
            elves = new_elves
        
        condition_def = [*condition_def[1:], condition_def[0]]
        
        if n_rounds is not None and r == n_rounds:
            break
            
    r_min, r_max, c_min, c_max = get_bounds(elves)
    n_empty = (r_max - r_min + 1) * (c_max - c_min + 1) - len(elves)
    return n_empty, r

n_empty, n_rounds = move(copy.deepcopy(elves), init_conditions, n_rounds = 10)

print(n_empty)

# part 2

n_empty, n_rounds = move(copy.deepcopy(elves), init_conditions)

print(n_rounds)