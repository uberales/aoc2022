#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:27:38 2022

@author: podolnik
"""

def l2m(line):
    pts = line.strip().split(': ')
    name = pts[0]
    pts = pts[1].split(' ')
    val = None
    m_a = None
    m_b = None
    op = None
    if len(pts) == 1:
        val = int(pts[0])
    else:
        m_a = pts[0]
        m_b = pts[2]
        op = pts[1]
        
    return name, (val, op, m_a, m_b)

with open('input.txt', 'r') as f:
    monkeys = dict([l2m(l) for l in f.readlines()])

# part 1

def eval_monkey(m, monkeys, cache):
    if m in cache:
        return cache[m]
    v = 0    
    if m[0] is not None:
        v = m[0]
    elif m[1] == '+':
        v = eval_monkey(monkeys[m[2]], monkeys, cache) + eval_monkey(monkeys[m[3]], monkeys, cache)
    elif m[1] == '-':
        v = eval_monkey(monkeys[m[2]], monkeys, cache) - eval_monkey(monkeys[m[3]], monkeys, cache)
    elif m[1] == '*':
        v = eval_monkey(monkeys[m[2]], monkeys, cache) * eval_monkey(monkeys[m[3]], monkeys, cache)
    elif m[1] == '/':
        v =eval_monkey(monkeys[m[2]], monkeys, cache) / eval_monkey(monkeys[m[3]], monkeys, cache)
    
    cache[m] = v
    return v
    
r = eval_monkey(monkeys['root'], monkeys, {})
print(r)

# part 2

m_a = monkeys[monkeys['root'][2]]
m_b = monkeys[monkeys['root'][3]]

sgn_prev = False
    
i = 0
d = 100000000000

while True:
    monkeys['humn'] = (i, None, None, None)
    a = eval_monkey(m_a, monkeys, {})
    b = eval_monkey(m_b, monkeys, {})
    sgn_this = a < b

    if a == b:
        break
    
    if sgn_prev != sgn_this:
        d = -(d + 1) // 2
    i += d
        
    sgn_prev = sgn_this

print(i)