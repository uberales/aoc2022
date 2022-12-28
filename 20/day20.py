#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:30:47 2022

@author: podolnik
"""

with open('input.txt', 'r') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

# part 1

def print_simple(first):   
    temp = first
    s = ''
    for i in range(len(numbers)):
        s += '{} '.format(temp.n)
        temp = temp.next
    print(s)
        
class Node:
    def __init__(self, n, i):
        self.n = n
        self.i = i
        self.next : Node = None
        self.prev : Node = None
        
    def get_by_offset(self, offset = None):
        offset = self.n if offset is None else offset
        temp = self
        for _ in range(abs(offset)):
            if offset < 0:
                temp = temp.prev
            else:
                temp = temp.next
        return temp
        
    def shuffle(self, mod = None):
        n_sw = self.n
        if mod is not None:
            n_sw = self.n % (mod - 1)
            if self.n < 0:
                n_sw -= mod - 1
        for _ in range(abs(n_sw)):
            if n_sw < 0:
                self.switch_prev()
            elif n_sw > 0:
                self.switch_next()
        
    def switch_prev(self):   
        other = self.prev
        
        sn = self.next
        op = other.prev
        
        self.next = other
        self.prev = op
        other.next = sn
        other.prev = self
        
        sn.prev = other
        op.next = self
    
    def switch_next(self):     
        other = self.next
        
        sp = self.prev
        on = other.next
        
        self.next = on
        self.prev = other
        other.next = self
        other.prev = sp
        
        sp.next = other
        on.prev = self      
        
        
    def __str__(self):
        s = '[{}: {}]'.format(self.i, self.n)
        if self.prev is not None:
            s = '({}: {}) -> '.format(self.prev.i, self.prev.n) + s
        if self.next is not None:
            s += ' -> ({}: {})'.format(self.next.i, self.next.n)
        return s

def get_nodes(numbers, mul = 1):

    nodes = [Node((n * mul), i) for i, n in enumerate(numbers)]
    
    first = nodes[0]
    zero = None
    for i in range(len(nodes)):
        i_next = (i + 1) % len(nodes)
        nodes[i].next = nodes[i_next]
        nodes[i_next].prev = nodes[i]
        if nodes[i].n == 0:
            zero = nodes[i]
    return first, zero, nodes

first, zero, nodes = get_nodes(numbers)
    
for i, node in enumerate(nodes):
    node.shuffle(mod=len(numbers))
    
a = zero.get_by_offset(offset=1000).n
b = zero.get_by_offset(offset=2000).n
c = zero.get_by_offset(offset=3000).n
 
print(a, b, c, '=>', a + b + c)

# part 2

first, zero, nodes = get_nodes(numbers, mul = 811589153)
mod = len(numbers)

for it in range(10):
    for i, node in enumerate(nodes):
        node.shuffle(mod = mod)
    
a = zero.get_by_offset(offset=1000).n
b = zero.get_by_offset(offset=2000).n
c = zero.get_by_offset(offset=3000).n
 
print(a, b, c, '=>',  a + b + c)