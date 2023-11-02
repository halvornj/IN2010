import math

line = input().strip().split()
while line != ["0", "0"]:
    n,d = int(line[0]), int(line[1])
    koeff = math.floor(n/d)
    print(f"{str(koeff)} {str(n%d)} / {str(d)}")
    line=input().strip().split()