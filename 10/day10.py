#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:19:44 2022

@author: podolnik
"""

def l2d(l):
    pts = l.strip().split(' ')
    ins = pts[0]
    val = int(pts[1]) if len(pts) > 1 else 0
    return (ins, val)

with open('input.txt', 'r') as f:
    commands = [l2d(l) for l in f.readlines()]
    
# part 1
val_x = 1
cycle = 1
stats = []

for cmd in commands:
    start = cycle
    end = cycle
    x_no2 = val_x
    dx = 0
    if cmd[0] == 'noop':
        end += 1
    elif cmd[0] == 'addx':
        end += 2
        dx = cmd[1]
    for s in range(start, end):
        stats.append(val_x)
    val_x += dx    
    cycle = end
        
stops = [20, 60, 100, 140, 180, 220]

print(sum([s*stats[s - 1] for s in stops]))

# part 2
w = 40
for r in range(0, 6*w, w):
    sprite = stats[r:r+w]
    pixels = [' ' for _ in range(w)]
    for i in range(w):
        p = (sprite[i]-1, sprite[i], sprite[i] + 1)
        if i in p:
            pixels[i] = '#'
    print(''.join(pixels))