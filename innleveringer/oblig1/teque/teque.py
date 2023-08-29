import math

class Node:
    def __init__(self, data):
        self.data = data
        self.prev:Node = None
        self.next:Node = None

    def getPrev(self):return self.prev
    def getNext(self): return self.next
    def setPrev(self, n):self.prev = n
    def setNext(self, n):self.next = n
    def getData(self):return self.data
class Teque:
    def __init__(self):
        self.head : Node = None
        self.middle : Node= None
        self.tail : Node = None
        self.size : Node= 0

    def emptyPush(self, x:Node):
        newNode : Node = Node(x)
        self.head = newNode
        self.tail = newNode
        self.middle = newNode
        self.size +=1

    #todo write Teque methods
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

    def get(self, i:int) ->object:
        #todo define 4 ranges and traverse based on these ranges
        if i in range(0, math.floor(self.size/4)):
            #trav forward from head
            print("forward from head")
            current : Node = self.head
            for j in range(i):
                current = current.getNext()
            return current.getData()
        elif i in range(math.floor(self.size/4), math.floor(self.size/2)):
            #traverse back from mid
            print("backward from mid")
            current : Node = self.middle
            distance : int = math.floor(self.size /2)
            for j in range(distance):
                current = current.getPrev()
            return current.getData()
        elif i in range(math.floor(self.size/2), math.floor(self.size*(3/4))):
            #traverse forward from mid
            print("forward from mid")
            current : Node = self.middle
            for j in range(i):
                current = current.getNext()
            return current.getData()
        else:
            #traverse back from tail
            print("backward from tail")
            current : Node = self.tail
            distance : int = math.floor(self.size /2)
            for j in range(distance):
                current = current.getPrev()
            return current.getData()

    def __str__(self):
        printstr : str = "["
        for i in range(len(self)):
            printstr +=self.get(i)
            printstr +=","
        printstr +="]"
        return printstr
    
    #todo override __len__():
    def __len__(self):
        return self.size


def main():
    teq : Teque = Teque()
    teq.push_back("d")
    teq.push_front("b")
    teq.push_front("a")
    teq.push_back("e")
    teq.push_middle("c")

    print(len(teq))
    print(teq.get(0))
    print(teq.get(1))
    print(teq.get(2))
    print(teq.get(3))

main()