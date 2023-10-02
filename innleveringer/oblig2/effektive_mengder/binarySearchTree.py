from node import Node
from typing import Generic
from typing import TypeVar

#TODO check that generic type T makes sense
#TODO docstrings

T = TypeVar('T')

#*for litt mer forventet oppførsel, der klassen er mer black-box og andre programm ikke trenger holde styr på root og Noder osv, er implementasjonen modifisert for å kun ta element X.
#gjør Generiske typer koden mye tregere? ja. (https://github.com/python/cpython/issues/83349). Gjør jeg det uansett fordi jeg liker statiske typer? ja :)
class BinarySearchTree(Generic[T]):
    def __init__(self):
        self._size:int = 0  #MÅ ha en metode som heter size() ifølge oppgaven, så denne må hete noe annet. ville heller bare brukt len() men jaja
        self.root:Node = None

    def insert(self, x:T) ->T:
        if self._size == 0:
            self.root = Node(x)
            self._size+=1
            return self.root.element
        return self.rec_insert(x, node=self.root).element


    def rec_insert(self, x:T, node:Node = None) ->Node:
        if node is None: 
            node = Node(x)
            self._size += 1
        elif x < node.element: node.left = self.rec_insert(x, node=node.left)
        elif x > node.element: node.right = self.rec_insert(x, node=node.right)
        return node
    
    def search(self, x:T) ->T:
        return self.rec_search(self.root, x)
    
    def rec_search(self, node:Node, x:T) -> T:
        if node == None:return None
        if node.element == x:return node.element
        if x < node.element: return self.rec_search(node.left, x)
        if x> node.element:return self.rec_search(node.right, x)

    def contains(self, x:T) ->bool:
        return (self.search(x) is not None) #antar her at du ikke vil ha et binary-tree fyllt med None-values :/

    def findMin(self, node:Node) ->Node:
        if not node.left :return node
        return self.findMin(node.left)
    
    def remove(self, x:T):
        self._size -=1
        return self.rec_remove(x, self.root)
    
    def rec_remove(self, x:T, node:Node):
        if node == None:return None
        if x < node.element:
            node.left = self.rec_remove(x, node.left)
            return node
        if x > node.element:
            node.right = self.rec_remove(x, node.right)
        if node.left == None: return node.right
        if node.right == None:return node.left
        u = self.findMin(node.right)
        node.element = u.element
        node.right = self.rec_remove(u.element, node.right)
        return node
    
    def size(self):
        return self._size

    def __len__(self):
        return self._size
    
    #todo def __str__ med DFS, left to right -> small to large
  