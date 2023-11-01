line = input()
out = ""
for i in range(1, len(line)):
    if line[i] == line[i-1]:continue
    out+=line[i]
if line[0] != out[0]:
    out = line[0]+out
print(out)