from node import Node


class BinarySearchTree:
    def __init__(self):
        self.size:int = 0
        self.root:Node = None

    def insert(self, node:Node, x:object) ->Node:

        if node is None: node = Node(x)
        elif x < node.element: node.left = self.insert(node.left,x)
        elif x > node.element: node.right = self.insert(node.right, x)
        return node
    