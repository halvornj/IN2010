from binarySearchTree import BinarySearchTree 

def test():
    tree = BinarySearchTree[int]()
    print(tree)
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(-1)
    tree.insert(-2)

    print(len(tree))
    print(tree.root)

    print(f"{tree.contains(0)=}")
    print(f"{tree.remove(0)=}")
    print(f"{tree.contains(0)=}")

    print(f"{tree.contains(1)=}")
    print(f"{tree.remove(1)=}")
    print(f"{tree.contains(1)=}")


test()