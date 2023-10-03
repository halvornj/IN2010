from binarySearchTree import BinarySearchTree 

def test():
    tree = BinarySearchTree[int]()
    print(tree)
    
    tree.insert(0)
    tree.insert(-1)
    tree.insert(1)
    tree.insert(-2)
    tree.insert(3)
    tree.insert(2)
    print(f"{tree.root=}")
    tree.remove(5)
test()