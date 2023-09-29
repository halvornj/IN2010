from node import Node
from typing import Generic
from typing import TypeVar

#TODO check that generic type T makes sense
#TODO docstrings

T = TypeVar('T')

#*for litt mer forventet oppførsel, der klassen er mer black-box og andre programm ikke trenger holde styr på root og Noder osv, er implementasjonen modifisert for å kun t
class BinarySearchTree(Generic(T)):
    def __init__(self):
        self.size:int = 0
        self.root:Node = None

    def insert(self, x:T):
        return self.rec_insert(self.root, x)

    def rec_insert(self, x:T, node:Node = None) ->Node:
        if node is None: node = Node(x)
        elif x < node.element: node.left = self.insert(node.left,x)
        elif x > node.element: node.right = self.insert(node.right, x)
        return node
    
    def rec_search(self, node:Node, x:T):
        if node == None:return None
        if node.element == x:return node.element
        if x < node.element: return self.rec_search(node.left, x)
        if x> v.element:return self.rec_search(node.right, x)