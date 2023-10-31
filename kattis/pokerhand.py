line = input().split()

counts = {}

for card in line:
    if card[0]in counts: counts[card[0]]+=1
    else: counts[card[0]] = 1
print(max(counts.values()))