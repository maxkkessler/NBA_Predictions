import random
import numpy as np
from numpy.linalg import matrix_power


#Practice to build a priority queue

class Node():
    def __init__(self, key, data):
        self.key = key
        self.data = data
    def __str__(self):
        s = '({}, {})'.format(self.key, self.data)
        return s

class Heap():
    def __init__(self):
        self.heap = [None]
    def left(self, i):
        return i*2
    def right(self, i):
        return (i*2)+1
    def parent(self,i):
        return i//2

    def insert(self, key, data):
        node = Node(key, data)
        self.heap.append(node)
        self.heapify_up()

    def heapify_up(self):
        i = len(self.heap)-1
        while (self.heap[self.parent(i)] != None) and (self.heap[i].key < self.heap[self.parent(i)].key):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapif_down(self):
        i = 1
        end = len(self.heap)-1

        while (self.right(i) <= end):
            right = self.right(i)
            left = self.left(i)
            l = self.heap
            lower_i = left

            if l[right].key < l[left].key:
                lower_i = right
            
            if l[i].key > l[lower_i].key:
                l[i], l[lower_i] = l[lower_i], l[i]
                i = lower_i
            else:
                break

        if (self.left(i) <= end) and (self.heap[i].key > self.heap[self.left(i)].key):
            self.heap[i], self.heap[self.left(i)] = self.heap[self.left(i)], self.heap[i]

    def extract_min(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        m = self.heap.pop()
        self.heapif_down()
        return m
    
    def __str__(self):
        l = []
        for i in self.heap[1:]:
            l.append(str(i))
        return str(l)


class Something():

    def __init__(self, something1, something2):
        self.one = something1
        self.two = something2


if __name__ == '__main__':
    x = 'hello'
    print(len(x))








    
        



