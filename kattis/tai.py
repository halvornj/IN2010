N = int(input())
total_area = 0

l = input().split()
previous_t = int(l[0])
previous_v = float(l[1])

for i in range(N-1):
    line = input().split()
    t = int(line[0])
    v = float(line[1])
    delta_t = t-previous_t
    total_area = (min(previous_v, v)*delta_t)+(abs(v-previous_v)*delta_t)/2
    previous_t = t
    previous_v = v
print(total_area)
