s = 0

n = int(input())
for i in range(n):
    l = input()
    won = True
    for i in range(1, len(l)):
        if l[i] == "D" and l[i-1]=="C":
            won = False
            print(f"lost {l}")
            break
    if won: s+=1
print(s)
