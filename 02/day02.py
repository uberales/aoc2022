#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:19:13 2022

@author: podolnik
"""

with open('input.txt', mode='r') as f:
    data = [tuple(l.strip().split(' ')) for l in f.readlines()]

rps_rules = {'A': ('Z', 'X', 1), 'B': ('X', 'Y', 2), 'C': ('Y', 'Z', 3)}

rps_rules = {
    ('A', 'X'): 1 + 3,    
    ('A', 'Y'): 2 + 6,    
    ('A', 'Z'): 3 + 0,
    ('B', 'X'): 1 + 0,    
    ('B', 'Y'): 2 + 3,    
    ('B', 'Z'): 3 + 6,
    ('C', 'X'): 1 + 6,    
    ('C', 'Y'): 2 + 0,    
    ('C', 'Z'): 3 + 3,
}

results = [rps_rules[m] for m in data]

print(sum(results))

rps_rules = {
    ('A', 'X'): 3 + 0,    
    ('A', 'Y'): 1 + 3,    
    ('A', 'Z'): 2 + 6,
    ('B', 'X'): 1 + 0,    
    ('B', 'Y'): 2 + 3,    
    ('B', 'Z'): 3 + 6,
    ('C', 'X'): 2 + 0,    
    ('C', 'Y'): 3 + 3,    
    ('C', 'Z'): 1 + 6,
}

results = [rps_rules[m] for m in data]

print(sum(results))
