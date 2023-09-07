from arrayteque import Teque

teq :Teque = Teque()



n = int(input())
for i in range(n):
    instruction, arg = input().split()
    if instruction == "get":
        print(teq.get(int(arg)))
    else: eval(f"teq.{instruction}{+arg})")

 