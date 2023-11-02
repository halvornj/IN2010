#idea: fill a buffer-array while input is name, 
#on num do the operation and flush buffer
SETNUM = 1
def order_set(num, setnum):
    part1 = []
    part2 = []
    for i in range(num):
        line = input().strip()
        if i%2 == 0:part1.append(line)
        else:part2.insert(0, line)
    set =part1+part2

    print(f"SET {setnum}")
    for el in set:
        print(el)


num = int(input())
while num != 0:
    order_set(num, SETNUM)
    SETNUM+=1
    num=int(input())