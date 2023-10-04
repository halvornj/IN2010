from typing import Generic
from typing import TypeVar
from binarySearchTree import BinarySearchTree

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, element:T, left=None, right=None, height = None):
        self.element:T = element
        self.left:Node|None = left
        self.right:Node|None = right
        self.height:int|None = height
    def __str__(self)->str:
        return str(self.element)
    
class AvlTree(BinarySearchTree[T]):
    def __init__(self):
        self._size:int = 0
        self.root: Node|None = None
    
    def height(self, node:Node|None)->int:
        """
        method that returns the height of a node, defined as the height of the highest sub-tree +1

        Parameters:
            node(Node|None): the root of the current sub-tree for which height should be found
        
        Returns:
            int: the height of the root for the current sub-tree.
        """
        height:int = -1
        if node is None:return height
        #sett høyde til det største av venstre subtre, så høyre subtre
        height = max(height, self.height(node.left))
        height = max(height, self.height(node.right))
        return height+1
    
    def setHeight(self, node:Node|None) ->None:
        """
        sets the height of a node, in respect to the highest sub-tree.

        Parameters:
            node(Node|None): the node the height should be set for.

        Returns:
            None.
        """
        if node is None: return
        node.height = 1+max(self.height(node.left), self.height(node.right))

    def leftRot(self, node:Node) ->Node:
        """
        method takes root of a sub-tree, and rotates the subtree left,
        meaning the right node of the original root becomes the new root.

        Parameters:
            node(Node): the root of the subtree to rotate

        Returns:
            Node: the root of the changed subtree
        """
        newRoot:Node = node.right #type:ignore , roterer aldri til None
        relocate:Node|None = newRoot.left 
        newRoot.left = node
        node.right = relocate
        self.setHeight(node)
        self.setHeight(newRoot)
        return newRoot
        
    def rightRot(self, node:Node) ->Node:
        """
        rotates a sub-tree to the left, meaning the left node of the root becomes the new root.

        Parameters:
            node(Node):the root of the subtree to rotate
        
        Returns:
            Node: the root of the rotated subtree.
        """
        newRoot:Node = node.left #type:ignore , roterer aldri til None
        relocate:Node|None = newRoot.right
        newRoot.right = node
        node.left = relocate
        self.setHeight(node)
        self.setHeight(newRoot)
        return newRoot
    
    def balanceFactor(self, node:Node|None) ->int:
        """
        todo docstring
        """
        if node is None: return 0
        return self.height(node.left)-self.height(node.right)

    #antar at man ikke vil rotere rundt None, det gir jo ikke mening, så supresser warnings her
    def balance(self, node:Node) ->Node:
        """
        todo docstring
        """
        if self.balanceFactor(node) < -1:
            if self.balanceFactor(node.right) > 0:
                node.right = self.rightRot(node.right)  #type:ignore
            return self.leftRot(node)
        if self.balanceFactor(node) > 1:
            if self.balanceFactor(node.left) < 0:
                node.left = self.leftRot(node.left) #type:ignore
            return self.rightRot(node)
        return node

    def insert(self, x:T)->Node|None:
        """
        todo docstring
        """
        if self._size == 0:
            self.root = Node(x)
            self._size+=1
            return self.root.element
        self.root=self.rec_insert(x, node=self.root)
        return self.root.element

    def rec_insert(self, x:T, node:Node|None) ->Node:
        """
        todo docstring
        """
        if node is None: 
            node = Node(x)
            self._size += 1
        elif x < node.element: node.left = self.rec_insert(x, node=node.left)
        elif x > node.element: node.right = self.rec_insert(x, node=node.right)
        self.setHeight(node)
        return self.balance(node)

    def rec_remove(self, x:T, node:Node|None) ->Node|None:
        """
        todo docstring
        """
        if node == None: 
            self._size+=1
            return None
        if x < node.element:
            node.left = self.rec_remove(x, node.left)
            return node
        if x > node.element:
            node.right = self.rec_remove(x, node.right)
            return node
        if node.left == None: return node.right
        if node.right == None:return node.left
        u = self.findMin(node.right) #type:ignore
        node.element = u.element
        node.right = self.rec_remove(u.element, node.right)
        self.setHeight(node)
        return self.balance(node)