#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:58:02 2022

@author: podolnik
"""

import json
from functools import cmp_to_key

def d2p(data):
    pts = [p.strip() for p in data.split('\n')]
    packet = []
    for p in pts[:2]:
        txt = '{{"val": {}}}'.format(p)
        packet.append(json.loads(txt)['val'])
    return tuple(packet)

with open('input.txt', 'r') as f:
    packets = [d2p(d) for d in f.read().split('\n\n')]

# part 1
def compare(a, b):
    if type(a) is int and type(b) is int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1        
    elif type(a) is list and type(b) is int:
        return compare(a, [b])
    elif type(a) is int and type(b) is list:
        return compare([a], b)
    else:
        m = max(len(a), len(b))
        for i in range(m):
            if i >= len(a):
                return -1
            elif i >= len(b):
                return 1
            else:
                c = compare(a[i], b[i])
                if c == 1:
                    return 1
                elif c == 0:
                    pass
                else:
                    return -1                
        return 0

correct = sum([i+1 if compare(p[0], p[1]) == -1 else 0 for i, p in enumerate(packets)])
print(correct)

# part 2
all_packets = [sp for p in packets for sp in p]
div2, div6 = [[2]], [[6]]
all_packets.extend([div2, div6])
all_packets.sort(key=cmp_to_key(compare))

i_2 = all_packets.index(div2) + 1
i_6 = all_packets.index(div6) + 1
print(i_2 * i_6)

