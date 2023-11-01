def get_grade(line):
    perc = int(input())
    if perc>=line[0]:return"A"
    if perc >=line[1]:return "B"
    if perc>=line[2]:return"C"
    if perc>=line[3]:return"D"
    if perc>=line[4]:return"E"
    return"F"
line = list(map(int, input().split()))
print(get_grade(line))

