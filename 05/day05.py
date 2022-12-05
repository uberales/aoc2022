#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:20:33 2022

@author: podolnik
"""

import re
import copy

with open('input.txt', mode='r') as f:
    buffer = []
    instructions = []
    
    buffer_loaded = False
    
    for l in f.readlines():
        if len(l) == 1:
            buffer_loaded = True
        elif buffer_loaded:
            m = re.match('move ([0-9]*) from ([0-9]*) to ([0-9]*)', l.strip())
            instructions.append([int(v) for v in (m[1], m[2], m[3])])
        else:
            buffer.append(l.replace('\n', ' '))
    
    keys = []    
    setup = {}     
    
    r = buffer.pop()
    keys = [int(r[i:i+4].strip()) for i in range(0, len(r), 4)]
    for k in keys:
        setup[k] = []
    
    while len(buffer) > 0: 
        r = buffer.pop()  
        for i in range(0, len(r), 4):
            k = keys[i//4]
            box = r[i:i+4].strip()
            if len(box) > 1:
                setup[k].append(box[1])
                
            
# part 1
warehouse = copy.deepcopy(setup)

for n_b, i_from, i_to in instructions:
    stack_stay, stack_move = warehouse[i_from][:-n_b], warehouse[i_from][-n_b:]
    warehouse[i_from] = stack_stay
    warehouse[i_to].extend(list(reversed(stack_move)))

top = ''.join([warehouse[k][-1] for k in warehouse])

print(top)  
                
# part 2
warehouse = copy.deepcopy(setup)

for n_b, i_from, i_to in instructions:
    stack_stay, stack_move = warehouse[i_from][:-n_b], warehouse[i_from][-n_b:]
    warehouse[i_from] = stack_stay
    warehouse[i_to].extend(stack_move)

top = ''.join([warehouse[k][-1] for k in warehouse])

print(top)
        
            
            