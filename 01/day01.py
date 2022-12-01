#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:11:38 2022

@author: podolnik
"""

# load input
with open('input.txt', mode='r') as f:
    data = f.read()
    elves = [[int(l) for l in s.split('\n') if l != ''] for s in data.split('\n\n')]
    
# part 1
sums = [sum(elf) for elf in elves]

max_calories = max(sums)

print(max_calories)

# part 2
sums.sort(reverse=True)

max_3 = sum(sums[:3])

print(max_3)