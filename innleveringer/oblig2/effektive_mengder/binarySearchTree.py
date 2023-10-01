from node import Node
from typing import Generic
from typing import TypeVar

#TODO check that generic type T makes sense
#TODO docstrings

T = TypeVar('T')

#*for litt mer forventet oppførsel, der klassen er mer black-box og andre programm ikke trenger holde styr på root og Noder osv, er implementasjonen modifisert for å kun ta element X.
class BinarySearchTree(Generic(T)):
    def __init__(self):
        self.size:int = 0
        self.root:Node = None

    def insert(self, x:T):
        size -= 1
        return self.rec_insert(x, node=self.root).element


    def rec_insert(self, x:T, node:Node = None) ->Node:
        if node is None: node = Node(x)
        elif x < node.element: node.left = self.insert(x, node=node.left)
        elif x > node.element: node.right = self.insert(x, node=node.right)
        return node
    
    def search(self, x:T) ->T:
        return self.rec_search(self.root, x)
    
    def rec_search(self, node:Node, x:T) -> T:
        if node == None:return None
        if node.element == x:return node.element
        if x < node.element: return self.rec_search(node.left, x)
        if x> node.element:return self.rec_search(node.right, x)


    def findMin(self, node:Node) ->Node:
        if not (node.left or node.right):return node
        node = node.left or node.right  #om .left eksisterer evales del 1 av uttrykket til true, og node blir assignet til node.left. ellers node.right
        return self.findMin(node)
    
    def rec_remove(self, x:T, node:Node):
        if node == None:return None
        if x < node.element:
            node.left = self.rec_remove(node.left, x)
            return node
        if x > node.element:
            node.right = self.rec_remove(node.right, x)
        if node.left == None: return node.right
        if node.right == None:return node.left
        u = self.findMin(node.right)
        node.element = u.element
        node.right = self.rec_remove(node.right, u.element)
        return node