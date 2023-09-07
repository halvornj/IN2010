import math
#TODO: docstrings

class Node:
    def __init__(self, data):
        self.data = data
        self.prev:Node = None
        self.next:Node = None

    #todo: decorators to make nicer get- and set-methods.
    def getPrev(self):return self.prev
    def getNext(self): return self.next
    def setPrev(self, n):self.prev = n
    def setNext(self, n):self.next = n
    def getData(self):return self.data

    def __str__(self):
        return str(self.prev.__class__) + ", "+self.data + ", "+str(self.next.__class__)
class Teque:
    def __init__(self):
        self.head : Node = None
        self.middle : Node= None
        self.tail : Node = None
        self.size : int= 0
        self.middleSwitch :bool = False

    def emptyPush(self, x):
        newNode : Node = Node(x)
        self.head = newNode
        self.tail = newNode
        self.middle = newNode
        self.size +=1

    #todo: push_back() and push_front() need to check if increase is 2, then middle needs to point back/ forward by 1
    def push_back(self, x):
        if self.size == 0: return self.emptyPush(x)
        newNode = Node(x)
        newNode.setPrev(self.tail)
        self.tail.setNext(newNode)
        self.tail = newNode
        self.size+=1
    def push_front(self,x):
        if self.size == 0: return self.emptyPush(x)
        newNode = Node(x)
        newNode.setNext(self.head)
        self.head.setPrev(newNode)
        self.head = newNode
        self.size+=1
    def push_middle(self, x):
        if self.size == 0: return self.emptyPush(x)
        newNode : Node = Node(x)
        if self.size % 2 == 0: 
            newNode.setPrev(self.middle)
            newNode.setNext(self.middle.getNext())
            self.middle.setNext(newNode)
        else: 
            newNode.setNext(self.middle)
            newNode.setPrev(self.middle.getPrev())
            self.middle.setPrev(newNode)
        self.middle = newNode
        self.size+=1

    """     
    def get(self, i:int) ->object:
        if i in range(0, math.floor(self.size/4)):
            #trav forward from head
            current : Node = self.head
            for j in range(i):
                current = current.getNext()
            return current.getData()
        elif i in range(math.floor(self.size/4), math.floor(self.size/2)):
            #traverse back from mid
            current : Node = self.middle
            distance : int = math.floor(self.size /2)
            for j in range(distance):
                current = current.getPrev()
            return current.getData()
        elif i in range(math.floor(self.size/2), math.floor(self.size*(3/4))):
            #traverse forward from mid
            current : Node = self.middle
            for j in range(math.floor(self.size/2)-i):
                current = current.getNext()
            return current.getData()
        else:
            #traverse back from tail
            current : Node = self.tail
            distance : int = self.size - i-1
            for j in range(distance):
                current = current.getPrev()
            return current.getData()
 """
    def get(self, i:int):
        current : Node = self.head
        for j in range(i):
            current = current.getNext()
        return current.getData()

    def __str__(self):
        printstr : str = "["
        for i in range(len(self)):
            printstr +=str(self.get(i))
            printstr +=","
        printstr = printstr[:-1]
        printstr +="]"
        return printstr
    
    def __len__(self):
        return self.size
