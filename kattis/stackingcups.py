n = int(input().strip())
def gen():
    i = 0
    while i<n:
        pair =input().strip().split()
        if pair[0].isdigit(): pair[0], pair[1] = pair[1],int(pair[0])/2
        yield(float(pair[1]), pair[0])
        i+=1
cups = {key: value for key, value in gen()}
for key in sorted(cups.keys()): print(cups[key])