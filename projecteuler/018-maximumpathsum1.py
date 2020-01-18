triangle = []
with open("018-triangle.py") as file:
    line = file.readline()
    while line:
        triangle.append([int(x) for x in line.split()])
        line = file.readline()

for i in range(1, len(triangle)):
    for j in range(1, len(triangle[i]) - 1):
        options = triangle[i - 1][j - 1: j + 1]
        triangle[i][j] = triangle[i][j] + max(options) 

print(triangle)