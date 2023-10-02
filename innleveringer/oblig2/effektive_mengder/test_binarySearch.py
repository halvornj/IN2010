from binarySearchTree import BinarySearchTree 

def test():
    tree = BinarySearchTree[int]()
    print(tree)
    print(type(tree))
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(-1)
    tree.insert(-2)

    print(len(tree))
    print(tree.root)
    print(tree.search(1))
    print(tree.contains(1))

    print(f"{tree.contains(0)=}")
    print(f"{tree.remove(0)=}")
    print(f"{tree.contains(0)=}")

    tree.remove(1)
    print(tree.search(1))
    print(tree.contains(1))


test()