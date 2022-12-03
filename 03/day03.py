#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:34:10 2022

@author: podolnik
"""

with open('input.txt', mode='r') as f:
    data = [l.strip() for l in f.readlines()]    
    rucksacks = [(r[:len(r)//2], r[len(r)//2:]) for r in data]

# part 1

priorities = {**{chr(i + ord('a')): i + 1 for i in range(26)}, **{chr(i + ord('A')): i + 27 for i in range(26)}}
    
p_sum = 0

for r in rucksacks:
    common = set(r[0]).intersection(set(r[1]))
    for c in common:
        p_sum += priorities[c]

print(p_sum)

# part 2

p_sum = 0

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    common = set(group[0][0]).union(group[0][1])
    for i in range(1, len(group)):
        common = common.intersection(set(group[i][0]).union(group[i][1]))
            
    badge = common.pop()
    p_sum = p_sum + priorities[badge]

print(p_sum)
