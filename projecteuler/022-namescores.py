names = []

with open("022-names.csv") as file:
    line = file.readline().strip('"').split('","')
    names = sorted(line)
    
scores = {chr(i): i - 64 for i in range(65, 91)}

total = 0

for i in range(len(names)):
    for j in range(len(names[i])):
        total += scores[names[i][j]] * (i + 1)

print(total)