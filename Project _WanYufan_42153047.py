#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, key = None, next=None):
        self.key = key
        self.next = next


class CompleteBinaryTree:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.size = 0
    
    def add(self,key):
        new_node = Node(key)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        
    def parent(self,i):
        if i == 0:
            return None
        else:
            return (i - 1) // 2
    
    def left_child(self,i):
        return 2 * i + 1
    
    def right_child(self.i):
        return 2 * i + 2
    
    def get(self, i):
        """return the node with index i"""
        pass
    

class MinPriorityQueue:
    def __init__(self):
        self.tree = CompleteBinaryTree()

    def insert(self, key):
        self.tree.add(key)
        i = self.tree.size - 1
        while i > 0 and self.tree.get(self.tree.parent(i)).key > self.tree.get(i).key: #from the element added last,compare with its parent
            self.tree.get(i).key, self.tree.get(self.tree.parent(i)).key = self.tree.get(self.tree.parent(i)).key, self.tree.get(i).key
            i = self.tree.parent(i) # if the parent is bigger, then swap with its parent
    def delMin(self):
        if self.tree.size == 0: # when the tree is empty
            return None
        if self.tree.size == 1: # when the tree contains only one element
            self.tree.size -= 1
            return self.tree.get(0).key
        min_val = self.tree.get(0).key # when the tree contains more than one elements, then the minimum is the root(the first one)
        self.tree.get(0).key = self.tree.get(self.tree.size - 1).key #swap the root(has been deleted) with the last to join
        self.tree.size -= 1
        i = 0
        while i < self.tree.size // 2: # make sure when it touch the lowest floor, then stop
            smallest_child = self.tree.left_child(i)
            if self.tree.right_child(i) < self.tree.size and self.tree.get(smallest_child).key > self.tree.get(self.tree.right_child(i)).data:
                smallest_child = self.tree.right_child(i) 
                """compare the smallest_child's left child and right child, then change the smallest_child to the smaller one"""
            if self.tree.get(i).key > self.tree.get(smallest_child).key:
                self.tree.get(i).key, self.tree.get(smallest_child).key = self.tree.get(smallest_child).key, self.tree.get(i).key 
                """swap the smaller child with the its parent"""
                i = smallest_child
            else:
                break
        return min_val
    
    
#performance benchmark for the linked list based heap
import time 
import random

if __name__ == "__main__":
    n = 10000
    pq = MinPriorityQueue()
    start_time = time.time()
    for i in range(n):
        pq.insert(random.random(0,100))
    end_time = time.time()
    print end_time - start_time
    start_time = time.time()
    for i in range(n):
        pq.delMin()
    end_time = time.time()
    print end_time - start_time
    
    
# Graphviz I am learning this program temporarily. If there is something wrong, I hope the teacher can show mercy，Thank a lot!
import graphviz

def visualize_heap(pq):
    dot = graphviz.Digraph()
    for i in range(pq.tree.size):
        dot.node(str(i),str(pq.tree.get(i).key)) # Create an element and number it
        if i != 0:
            dot.edge(str(pq.tree.parent(i)),str(i)) # line the parent element with the child
    return dot

