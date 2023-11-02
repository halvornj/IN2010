#birthdays[date] -> (name, priority)
birthdays = {}

N = int(input())

for i in range(N):
    line = input().split()
    if birthdays.get(line[2], None) == None:
        birthdays[line[2]]= (line[0], line[1])
    else:
        if int(birthdays[line[2]][1]) < int(line[1]):
            birthdays[line[2]] = (line[0], line[1])

print(len(birthdays))
names = list(birthdays.values())
names.sort(key=lambda x:x[0])
for name in [x[0] for x in names]:
    print(name)