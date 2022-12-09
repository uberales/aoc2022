#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:08:21 2022

@author: podolnik
"""

import numpy as np

with open('input.txt', 'r') as f:
    data = [l.strip().split(' ') for l in f.readlines()]
    data = [(r[0], int(r[1])) for r in data]
    
# part 1
directions = {'L': (0, -1), 'R': (0, 1), 'D': (-1, 0), 'U': (1, 0)}

def follow(head, tail):
    dr = head[0] - tail[0]
    dc = head[1] - tail[1]
    
    r, c = tail
    
    if np.sqrt(dr*dr + dc*dc) < 2:
        return r, c
    
    if abs(dr) > 0:
        r += dr // abs(dr)
    if abs(dc) > 0:
        c += dc // abs(dc)
    
    return r, c


head = (0, 0)
tail = (0, 0)

tail_history = set()
tail_history.add(tail)

for move in data:
    for _ in range(move[1]):
        d = directions[move[0]]
        head = (head[0] + d[0], head[1] + d[1])
        tail = follow(head, tail)
        tail_history.add(tail)
        
print(len(tail_history))

# part 2
rope = [(0, 0) for _ in range(10)]

tail_history = set()
tail_history.add(rope[-1])

for move in data:
    for _ in range(move[1]):
        d = directions[move[0]]
        rope[0] = (rope[0][0] + d[0], rope[0][1] + d[1])        
        for i in range(1, len(rope)):
            rope[i] = follow(rope[i - 1], rope[i])
        tail_history.add(rope[-1])
            
print(len(tail_history))

            