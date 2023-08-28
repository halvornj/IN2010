class Node:
    def __init__(self, data):
        self.data = data
        self.prev:Node = None
        self.next:Node = None
class Teque:
    def __init__(self):
        self.head : Node = None
        self.middle : Node= None
        self.tail : Node = None
        self.size : Node= 0
    def __init__(self, data):
        self.head : Node= Node(data)
        self.middle :Node = self.head
        self.tail:Node= self.head
        self.size:int = 1
    #todo write Teque methods
    def push_back(self, x):
        newNode = Node(x)
        self.tail.next = newNode
        self.tail = newNode
        size+=1
    def push_front(self,x):
        newNode = Node(x)
        self.head.prev = newNode
        self.head = newNode
        size+=1
    def push_middle(self, x):
        newNode : Node = Node(x)
        if self.size % 2 == 0: self.middle.next = newNode
        else: self.middle.prev = newNode
        self.middle = newNode
        size+=1

    def get(self, i:int) ->object:
        #todo define 4 ranges and traverse based on these ranges
        
        pass