line = input()
counts = {}
sum = 0
for char in line:
    counts[char] +=1
values = list(counts.values())
for val in values:
    sum +=val**2
sum += 7*min(values)
print(sum)
