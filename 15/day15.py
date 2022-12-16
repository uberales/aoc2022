#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 09:11:56 2022

@author: podolnik
"""

import re
import numpy as np

def manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def d2s(data):
    vals = [int(v) for v in data]
    s = (vals[0], vals[1])
    b = (vals[2], vals[3])
    return s, b, manhattan(s, b)

with open('input.txt', 'r') as f:
    txt = f.read()
    data = re.findall('Sensor at x=([-0-9]*), y=([-0-9]*): closest beacon is at x=([-0-9]*), y=([-0-9]*)', txt)
    sensors = [d2s(d) for d in data]

# part 1
    
def in_range(coords, base, radius):
    return manhattan(coords, base) <= radius

def get_bounds(sensor, beacon):
    r = manhattan(sensor, beacon)
    return sensor[0] - r, sensor[0] + r, sensor[1] - r, sensor[1] + r

y_ref = 2000000
beacons = set([s[1] for s in sensors])
not_possible = set()

for s in sensors:
    x_min, x_max, y_min, y_max = get_bounds(s[0], s[1])    
    if y_min <= y_ref and y_max >= y_ref:
        dx = s[2] - abs(y_ref - s[0][1])
        x_min = s[0][0] - dx
        x_max = s[0][0] + dx
        restricted = [(x, y_ref) for x in range(x_min, x_max + 1)]
        not_possible = not_possible.union(restricted)
    
not_possible = not_possible.difference(beacons)
print(len(not_possible))

# part 2
"""
I am obviously stupid, however, this works only if the point surroundings are 
covered by at least two beacons. Fortunately, I got a proper input.
"""

def in_any(sensors, pt):
    for s in sensors:
        if in_range(pt, s[0], s[2]):
            return True
    return False

def get_square(sensor, beacon):
    r = manhattan(sensor, beacon)
    return (sensor[0], sensor[1] - r), (sensor[0] + r, sensor[1]), (sensor[0], sensor[1] + r), (sensor[0] - r, sensor[1])

def intersect(sq_a, sq_b):
    def pt2lin(pt_0, pt_1):
        a = (pt_1[1] - pt_0[1]) / (pt_1[0] - pt_0[0])
        b = pt_0[1] - a * pt_0[0]
        return a, b    
    
    def intersect_line(start_0, end_0, start_1, end_1):        
        a_0, b_0 = pt2lin(start_0, end_0)
        a_1, b_1 = pt2lin(start_1, end_1)
        if a_0 == a_1:
            return set()
        x = (b_1 - b_0) / (a_0 - a_1)
        y = a_0 * x + b_0
        
        lt = min(start_0[0], end_0[0])
        rt = max(start_0[0], end_0[0])
        
        if x >= lt and x <= rt:
            if abs(x % 1) == 0.5 and abs(y % 1) == 0.5:
                ret = set()
                ret.add((int(x // 1), int(y // 1)))
                ret.add((int(x // 1) + 1, int(y // 1)))
                ret.add((int(x // 1), int(y // 1) + 1))
                ret.add((int(x // 1) + 1, int(y // 1) + 1))
                return ret
            else:
                return set([(int(x), int(y))])
        return set()
    
    intersections = set()
    
    for i in range(4):
        start_0 = sq_a[i]
        end_0 = sq_a[(i + 1) % 4]
            
        for j in range(4):
            start_1 = sq_b[j]
            end_1 = sq_b[(j + 1) % 4]
            
            pts = intersect_line(start_0, end_0, start_1, end_1)
            intersections = intersections.union(pts)
    return intersections

all_intersections = set()

bounds = ((0, 4000000), (0, 4000000))   
# bounds = ((0, 20), (0, 20))    

def check_bounds(pt, bounds):
    return pt[0] >= bounds[0][0] and pt[0] <= bounds[0][1] and pt[1] >= bounds[1][0] and pt[1] <= bounds[1][1] 

for sensor_a in sensors:
    sq_a = get_square(sensor_a[0], sensor_a[1])
    for sensor_b in sensors:
        sq_b = get_square(sensor_b[0], sensor_b[1])
        
        points = set([pt for pt in intersect(sq_a, sq_b) if check_bounds(pt, bounds)])
        all_intersections = all_intersections.union(points)

def get_neighbors(pt):
    neighbors = set([(pt[0] + dx, pt[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]])
    return neighbors

neighbors = set.union(*[get_neighbors(pt) for pt in all_intersections])
    
def add_bounds(int_pts, bounds):
    x = bounds[0][0] - 1
    for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
        int_pts.add((x, y))
    x = bounds[0][1] + 1
    for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
        int_pts.add((x, y))    
    y = bounds[1][0] - 1
    for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
        int_pts.add((x, y))
    y = bounds[1][1] + 1
    for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
        int_pts.add((x, y))
        
add_bounds(all_intersections, bounds)

candidates = set()

for pt in neighbors:
    c = sum([p in all_intersections for p in get_neighbors(pt)])
    if c == 4 and not in_any(sensors, pt):
        candidates.add(pt)
        
for c in candidates:
    print(c[0] * 4000000 + c[1])