#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:57:09 2022

@author: podolnik
"""

with open('input.txt', 'r') as f:
    cubes = [tuple([int(v) for v in l.strip().split(',')]) for l in f.readlines()]

# part 1

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0) , (0, 0, -1), (0, 0, 1)]

def get_faces(origin):
    result = set()
    for d in directions:
        result.add((d[0]/2 + origin[0], d[1]/2 + origin[1], d[2]/2 + origin[2]))
    return result

def get_surface(cubes):
    facing_out = set()
    for c in cubes:
        faces = get_faces(c)
        for f in faces:
            if f in facing_out:
                facing_out.remove(f)
            else:
                facing_out.add(f)
    return facing_out

total_surface = get_surface(cubes)

print(len(total_surface))

# part 2
    
x_min = min([c[0] for c in cubes]) - 1
x_max = max([c[0] for c in cubes]) + 1
y_min = min([c[1] for c in cubes]) - 1
y_max = max([c[1] for c in cubes]) + 1
z_min = min([c[2] for c in cubes]) - 1
z_max = max([c[2] for c in cubes]) + 1

def print_cubes(cubes):
    for x in range(x_min, x_max + 1):        
        for y in range(y_min, y_max + 1):            
            row = ''
            for z in range(z_min, z_max + 1):
                if (x, y, z) in cubes:
                    row += 'X'
                else:
                    row += '.'
            print(row)
        print()
            

def get_neighbors(x, y, z):
    def check_bounds(v, v_min, v_max):
        return v >= v_min and v <= v_max
    result = []
    for d in directions:
        c = (x + d[0], y + d[1], z + d[2])
        if check_bounds(c[0], x_min, x_max) and check_bounds(c[1], y_min, y_max) and check_bounds(c[2], z_min, z_max):
            result.append(c)
    return result

all_cubes = set()
for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        for z in range(z_min, z_max + 1):
            all_cubes.add((x, y, z))
            
queue = [(x_min, y_min, z_min)]

outer_cubes = set()
while len(queue) > 0:
    c_mid = queue.pop(0)
    if c_mid not in cubes and c_mid not in outer_cubes:
        outer_cubes.add(c_mid)
        queue.extend(get_neighbors(*c_mid))
        
inner_cubes = all_cubes.difference(outer_cubes)

outer_surface = get_surface(inner_cubes)

print_cubes(outer_cubes)

print(len(outer_surface))