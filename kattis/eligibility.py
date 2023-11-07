N = int(input().strip())

def findElig(name, start, born, courses):
    if int(start.split("/")[0])>2009:
        return(name +" eligible")
    if int(born.split("/")[0])>1990:
        return(name+" eligible")
    if courses >40:
        return(name +" ineligible")
    return(name + " coach petitions")


for i in range(N):
    line = input().strip().split()
    name, start, born, courses = line[0],line[1], line[2], int(line[3])
    print(findElig(name, start, born, courses))