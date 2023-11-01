#birthdays[date] -> (name, prioriyt)
birthdays = {}

N = int(input())

for i in range(N):
    line = input().split()
    if birthdays[line[2]] == None:
        birthdays[line[2]]= (line[0], line[1])