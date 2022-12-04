#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:38:51 2022

@author: podolnik
"""

def l2d(l):
    p = l.split(',')
    a = p[0].split('-')
    b = p[1].split('-')
    return (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))

with open('input.txt', mode='r') as f:
    data = [l2d(l.strip()) for l in f.readlines()]
    
# part 1    

n_valid = 0

for d in data:
    sgn = (d[0][0] - d[1][0]) * (d[0][1] - d[1][1])
    n_valid += 1 if sgn <= 0 else 0

print(n_valid)

# part 2

n_valid = 0

for d in data:    
    d_s = sorted(d, key=lambda v: v[0])
    n_valid += 1 if d_s[1][0] <= d_s[0][1] else 0

print(n_valid)