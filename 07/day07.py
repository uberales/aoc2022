#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:20:15 2022

@author: podolnik
"""

commands = []

with open('input.txt', mode='r') as f:
    for l in f.readlines():
        l = l.strip()
        if l[0] == '$':
            c = l[1:].strip().split(' ')
            cmd = (c, [])
            commands.append(cmd)
        else:
            o = [int(p) if p.isnumeric() else p for p in l.split(' ')]
            commands[-1][1].append(tuple(o))

# part 1

root = 'fs:/'
filesystem = {root: []}
current_path = root

def cd_up(path):
    if path == root:
        return None
    pts = path.split('/')[:-1]
    path = '/'.join(pts) 
    if len(pts) == 1:
        path += '/'
    return path

for cmd in commands:
    c_str = cmd[0][0]
    if c_str == 'cd':
        cd_to = cmd[0][1]
        if cd_to[0] == '/':
            current_path = root + cd_to[1:]
        elif cd_to == '..':
            current_path = cd_up(current_path)
        else:
            current_path += cd_to if current_path[-1] == '/' else '/' + cd_to        
    elif c_str == 'ls':
        dir_contents = cmd[1]
        for file in dir_contents:
            if file[0] == 'dir':
                dir_path = current_path + (file[1] if current_path[-1] == '/' else '/' + file[1])
                filesystem[dir_path] = []
            else:
                filesystem[current_path].append(file)
    
dir_sizes = {d: 0 for d in filesystem}

for d in filesystem:
    files = filesystem[d]
    for f in files:
        dir_from = d
        while dir_from is not None:
            dir_sizes[dir_from] += f[0]
            dir_from = cd_up(dir_from)

sum_dirs = sum([ds for _, ds in dir_sizes.items() if ds <= 100000])

print(sum_dirs)

# part 2

to_delete = 30000000 - (70000000 - dir_sizes[root])

smallest_d = min([ds for _, ds in dir_sizes.items() if ds >= to_delete])

print(smallest_d)

