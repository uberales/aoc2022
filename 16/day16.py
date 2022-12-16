#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:24:05 2022

@author: podolnik
"""

import re

pat = 'Valve ([A-Z]*) has flow rate=([0-9]*); tunnels* leads* to valves* ([, A-Z]*)'
    
def m2v(match):
    n = match[0]
    f = int(match[1])
    t = match[2].split(', ')
    return (n, f, t)

with open('input.txt', 'r') as f:
    txt = f.read()
    valves = [m2v(m) for m in re.findall(pat, txt)]
    
graph = {}
flow = {}
for v in valves:
    graph[v[0]] = list(v[2])
    flow[v[0]] = v[1]
    
def get_shortest(graph, start):
    shortest = {k: -1 for k in graph}
    queue = [start]
    shortest[start] = 0
    while len(queue) > 0:
        current = queue.pop(0)
        for node in graph[current]:
            if shortest[node] >= shortest[current] + 1 or shortest[node] == -1:
               shortest[node] = shortest[current] + 1
               queue.append(node)
    shortest = {k: v for k, v in shortest.items() if flow[k] > 0 and v > 0}
    return shortest

shortest = {k: get_shortest(graph, k) for k in graph if flow[k] > 0}

shortest['AA'] = get_shortest(graph, 'AA')

test_order = ('DD', 'BB', 'JJ', 'HH', 'EE', 'CC')

t_max = 30
max_flow = 0
max_path = None

def get_max_flow(graph, visited, total_flow, t_max):
    global max_flow
    global max_path    
        
    for node in shortest[visited[-1]]:
        if node not in visited:            
            t_remaining = t_max - (shortest[visited[-1]][node] + 1)
        
            new_flow = total_flow + flow[node] * t_remaining
            max_flow = max(max_flow, new_flow)     
                        
            if new_flow == max_flow:
                max_path = [*visited, node]
                
            if t_remaining > 0:                
                get_max_flow(graph, [*visited, node], new_flow, t_remaining)

get_max_flow(graph, ['AA'], 0, 30)

print(max_flow)
print(max_path)

max_flow = 0
max_path = None


def get_max_flow_1(graph, visited_a, visited_b, total_flow, t_max_a, t_max_b):
    global max_flow
    global max_path    
        
    for node in shortest[visited_a[-1]]:
        if node not in visited_a and node not in visited_b:            
            t_remaining = t_max_a - (shortest[visited_a[-1]][node] + 1)
        
            new_flow = total_flow + flow[node] * t_remaining
                        
            if new_flow > max_flow:
                max_flow = new_flow
                max_path = ([*visited_a], [*visited_b, node])
                print(new_flow, max_path)
                
            if t_remaining > 0:
                get_max_flow_1(graph, [*visited_a, node], visited_b, new_flow, t_remaining, t_max_b)      
                
                
    for node in shortest[visited_b[-1]]:
        if node not in visited_a and node not in visited_b:            
            t_remaining = t_max_b - (shortest[visited_b[-1]][node] + 1)
        
            new_flow = total_flow + flow[node] * t_remaining
            
            if new_flow > max_flow:
                max_flow = new_flow
                max_path = ([*visited_a], [*visited_b, node])
                print(new_flow, max_path)
                
            if t_remaining > 0:                
                get_max_flow_1(graph, visited_a, [*visited_b, node], new_flow, t_max_a, t_remaining)      
                
get_max_flow_1(graph, ['AA'], ['AA'], 0, 26, 26)

print(max_flow)
print(max_path)