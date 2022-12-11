#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:49:35 2022

@author: podolnik
"""

import copy

def d2m(monkeys, data):
    items = [int(i) for i in data[1].split(': ')[1].split(', ')]
    ins = data[2].split('new = ')[1]
    mod = int(data[3].split('divisible by ')[1])
    res_t = int(data[4].split('throw to monkey ')[1])
    res_f = int(data[5].split('throw to monkey ')[1])
        
    monkey = {'items': items, 'eval': ins, 'mod': mod, "t": res_t, "f": res_f}
    monkeys.append(monkey)

monkey_reserve = []

with open('input.txt', 'r') as f:
    data = []
    for l in f.readlines():
        if l == '\n':
            d2m(monkey_reserve, data)
            data = []
        else:
            data.append(l.strip())
    d2m(monkey_reserve, data)

# part 1
    
monkeys = copy.deepcopy(monkey_reserve)

activity = [0] * len(monkeys)

n_r = 20
for r in range(n_r):
    for i, m in enumerate(monkeys):
        for item in m['items']:
            activity[i] += 1
            w = eval(m['eval'].replace('old', '{}'.format(item))) // 3
            if w % m['mod'] == 0:
                monkeys[m['t']]['items'].append(w)
            else:
                monkeys[m['f']]['items'].append(w)
        m['items'] = []
    
        
activity.sort(reverse=True)
print(activity[0] * activity[1])

# part 2
monkeys = copy.deepcopy(monkey_reserve)

p_mod = 1
for m in monkeys:
    p_mod = p_mod * m['mod']

activity = [0] * len(monkeys)

n_r = 10000
for r in range(n_r):
    for i, m in enumerate(monkeys):
        for item in m['items']:
            activity[i] += 1
            w = eval(m['eval'].replace('old', '{}'.format(item)))
            if w % m['mod'] == 0:
                monkeys[m['t']]['items'].append(w % p_mod)
            else:
                monkeys[m['f']]['items'].append(w % p_mod)
        m['items'] = []
        
activity.sort(reverse=True)
print(activity[0] * activity[1])