#[("circle||rectangle", x,y,r ||x,y,x2,y2 ),()]
targets = []

def is_hit(target, shot):
    if target[0]=="rectangle":
        return (shot[0] in range(target[1], target[3]+1) and shot[1]in range(target[2], target[4]+1)) 
    elif target[0]=="circle":
        return (((shot[0] - target[1])**2 + (shot[1]-target[2])**2) < target[3]**2)
    else: raise ValueError("ooga booga")

m = int(input().strip())
for i in range(m):
    line = input().strip().split()
    if line[0]=="rectangle": targets.append((line[0],int(line[1]), int(line[2]), int(line[3]),int(line[4])))
    elif line[0]=="circle": targets.append((line[0], int(line[1]),int(line[2]),int(line[3])))
    else: raise ValueError("ooga booga")



n = int(input().strip())
for i in range(n):
    shot = list(map(int, input().strip().split()))
    hits = len([x for x in targets if is_hit(x, shot)])
    print(hits)
