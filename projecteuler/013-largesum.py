numbers = []
with open("013-numbers.txt") as file:
    line = file.readline()
    while line:
        numbers.append(int(line.strip()))
        line = file.readline()

print(str(sum(numbers))[:10])