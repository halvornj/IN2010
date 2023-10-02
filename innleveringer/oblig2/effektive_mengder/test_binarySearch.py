from binarySearchTree import BinarySearchTree 

def test():
    tree = BinarySearchTree[int]()
    print(tree)
    print(type(tree))
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(-1)

    print(len(tree))
    print(tree.root)
    print(tree.search(1))
test()