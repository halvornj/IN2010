from typing import Final
import math

class teque:
    
    def __init__(self):
        self.array : list = []
        self.head :int = 0
        self.tail :int = 0
        self.mid :int = lambda: math.floor(len(self.array)/2)
    
    def __init__(self, x):
        self.array :list = [x]
        self.head :int= 0
        self.tail :int= 1
        self.mid :int = lambda: math.floor(len(self.array)/2)


    def push_back(self, x):
        self.array.append(x)
    def push_front(self, x):
        self.array.insert(0, x)
    def push_middle(self, x):
        self.array.insert(self.mid, x)