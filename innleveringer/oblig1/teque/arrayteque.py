from typing import Final
import math

class Teque:
    
    def __init__(self):
        self.array : list = []


    def push_back(self, x):
        self.array.append(x)
    def push_front(self, x):
        self.array.insert(0, x)
    def push_middle(self, x):
        self.array.insert(math.ceil(len(self.array)/2), x)

    def get(self, i:int):
        return self.array[i]

    def __str__(self):
        outputStr: str = "["
        for el in self.array:
            outputStr += f"{str(el)}, "
        outputStr = outputStr[:-1] + "]"
        return outputStr
    def __len__(self):
        return len(self.array)
    
    #TODO __iter__() and __next__()

