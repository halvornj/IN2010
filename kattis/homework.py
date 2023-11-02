line = input().split(";")
count = 0

for problem in line:
    if "-" in problem:
        count +=(int(problem.split("-")[1])-int(problem.split("-")[0])+1)
    else:count+=1

print(count)