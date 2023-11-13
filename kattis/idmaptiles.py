from math import floor
s = input().strip()
zoom = len(s)
x, y = 0,0

min_x = 0
max_x = (zoom+1)*2-1
min_y = 0
max_y = (zoom+1)*2-1
#for x
for char in s:
    n = int(char)
    match char:
        case "0":
            max_x = floor(max_x/2)
            max_y = floor(max_y/2)
        case "1":
            min_x = floor(max_x/2)
            max_y = floor(max_y/2)

        case "2":
            max_x = floor(max_x/2)
            min_y = floor(max_y/2)
        case"3":
            min_x = floor(max_x/2)
            min_y = floor(max_y/2)

print(f"{min_x=}")
print(f"{max_x=}")
print(f"{min_y=}")
print(f"{min_y=}")

print(f"{zoom} {x} {y}")
