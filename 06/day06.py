#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:26:29 2022

@author: podolnik
"""

with open('input.txt', mode='r') as f:
    stream = list(f.read().strip())
    
# part 1

def find_marker(m_len, stream):
    for i in range(m_len, len(stream) + 1):
        sub = stream[i-m_len:i]
        if len(sub) == len(set(sub)):
            break
    return i
    
print(find_marker(4, stream))

# part 2
print(find_marker(14, stream))
