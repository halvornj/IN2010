coords = list(map(float, input().split()))
a = (coords[0], coords[1])
b = (coords[2],coords[3])
x = abs(a[0]-b[0])
y = abs(a[1]-b[1])
print(x*y)