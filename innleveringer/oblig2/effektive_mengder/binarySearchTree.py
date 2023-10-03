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
        self.root:Node|None = None  #note to self: "Node|None" er det samme som"Node?" i siviliserte språk (kotlin)

    def insert(self, x:T) ->T:
        """insert element into the set. all elements in the set must be of a comparable type.

        Parameters:
            x: the element to insert.

        Returns:
            x: the inserted element.
        
        """
        if self._size == 0:
            self.root = Node(x)
            self._size+=1
            return self.root.element
        return self.rec_insert(x, node=self.root).element


    def rec_insert(self, x:T, node:Node|None) ->Node:
        """private recursive method used to insert the element at the appropriate node.

        Parameters:
            x: the element to insert
            node (Node | None): the root of the current sub-tree from which the path to the appropriate insert-position can be found.

        Returns:
            Node: the new node containing x, or if it exists, the node already containing x.

        """
        if node is None: 
            node = Node(x)
            self._size += 1
        elif x < node.element: node.left = self.rec_insert(x, node=node.left)
        elif x > node.element: node.right = self.rec_insert(x, node=node.right)
        return node
    

    def search(self, x:T) ->T|None:
        return self.rec_search(self.root, x)
    

    def rec_search(self, node:Node|None, x:T) -> T|None:
        if node == None:return None
        if node.element == x:return node.element
        if x < node.element: return self.rec_search(node.left, x)
        if x> node.element:return self.rec_search(node.right, x)

    def contains(self, x:T) ->bool:
        return (self.search(x) is not None) #antar her at du ikke vil ha et binary-tree fyllt med None-values :/

    def findMin(self, node:Node) ->Node:
        if not node.left :return node
        return self.findMin(node.left)
    
    def remove(self, x:T)-> T | None:
        """removes an element from the set. 

        Parameters:
            x: the element to remove.

        Returns:
            the removed element if it existed in the set, otherwise None.
        """
        self._size -=1
        
        self.root = self.rec_remove(x, self.root)
        return self.root.element if self.root is not None else None
    

    def rec_remove(self, x:T, node:Node|None) ->Node|None:
        if node == None:
            return None
        if node.right is None and x > node.element: return node
        if node.left is None and x< node.element:return node
        if x < node.element:
            node.left = self.rec_remove(x, node.left)
            return node
        if x > node.element:
            node.right = self.rec_remove(x, node.right)
        #håndterer 0 eller 1 barnepeker, !this is wo die bug wohnt
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
    
    #todo def __str__ med DFS, left to right -> small to large -> sorted set
  