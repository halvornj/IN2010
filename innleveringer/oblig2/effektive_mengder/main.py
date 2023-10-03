from binarySearchTree import BinarySearchTree
def main():
    #! endre hva som deklareres som structure for å endre om programmet bruker binært søketre eller AVL-tre
    structure = BinarySearchTree[int]()
    n = int(input())
    for i in range(n):
        inp = input()
        if inp=="size":
            print(structure.size())
            continue
        instruction, arg = inp.split()
        if instruction == "contains":
            print(str(structure.contains(int(arg))).lower())
        else:
            eval(f"structure.{instruction}({int(arg)})")
        
if __name__=="__main__":main()