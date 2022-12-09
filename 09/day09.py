#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:08:21 2022

@author: podolnik
"""

import numpy as np
import matplotlib.pyplot as plt

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

tail_history_1 = set()
tail_history_1.add(tail)

for move in data:
    for _ in range(move[1]):
        d = directions[move[0]]
        head = (head[0] + d[0], head[1] + d[1])
        tail = follow(head, tail)
        tail_history_1.add(tail)
        
print(len(tail_history_1))

# part 2
rope = [(0, 0)] * 10

tail_history_2 = set()
tail_history_2.add(rope[-1])

for move in data:
    for _ in range(move[1]):
        d = directions[move[0]]
        rope[0] = (rope[0][0] + d[0], rope[0][1] + d[1])        
        for i in range(1, len(rope)):
            rope[i] = follow(rope[i - 1], rope[i])
        tail_history_2.add(rope[-1])
            
print(len(tail_history_2))

# visualisation

tail1 = sorted(tail_history_1)
tail1_r = [t[0] for t in tail1]
tail1_c = [t[1] for t in tail1]

tail2 = sorted(tail_history_2)
tail2_r = [t[0] for t in tail2]
tail2_c = [t[1] for t in tail2]

fig, ax = plt.subplots()
ax.scatter(tail1_c, tail1_r, s=1, label='#1', alpha = 0.5)
ax.scatter(tail2_c, tail2_r, s=1, label='#2', alpha = 0.5)
ax.set_xlabel('column')
ax.set_ylabel('row')
ax.set_aspect('equal')
ax.set_title('Tail location')
ax.legend()
plt.savefig('tail.png', bbox_inches='tight')
plt.show()
plt.close()