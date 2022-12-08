#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:13:57 2022

@author: podolnik
"""

import numpy as np

trees = []

with open('input.txt', mode='r') as f:
    trees = np.array([list(map(int, l.strip())) for l in f.readlines()])

# part 1
def get_visible(row):
    visible = np.zeros(np.shape(row), dtype=int)
    h_0 = -1
    for i in range(len(row)):
        if row[i] > h_0:
            visible[i] = 1
            h_0 = row[i]
    return visible

vis_l = np.array([get_visible(row) for row in trees])
vis_r = np.fliplr(np.array([get_visible(row) for row in np.fliplr(trees)]))
vis_t = np.array([get_visible(row) for row in trees.T]).T
vis_b = np.flipud(np.array([get_visible(row) for row in np.fliplr(trees.T)]).T)

vis = vis_l + vis_r + vis_t + vis_b

tot_vis = np.sum(vis > 0)
print(tot_vis)

# part 2
def get_scenic(row):
    score = np.zeros(np.shape(row), dtype=int)
    for i_0 in range(len(row)):
        h_0 = row[i_0]
        for i in range(i_0 + 1, len(row)):
            h = row[i]
            score[i_0] += 1            
            if h >= h_0:
                break
    return score

sce_r = np.array([get_scenic(row) for row in trees])
sce_l = np.fliplr(np.array([get_scenic(row) for row in np.fliplr(trees)]))
sce_d = np.array([get_scenic(row) for row in trees.T]).T
sce_u = np.flipud(np.array([get_scenic(row) for row in np.fliplr(trees.T)]).T)

sce = sce_r * sce_l * sce_d * sce_u
 

max_sce = np.max(sce)
print(max_sce)