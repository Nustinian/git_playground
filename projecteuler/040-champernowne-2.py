marks = [0]

def add_marks(times):
    for i in range(times):
        marks.append(marks[-1] + len(marks) * (9 * (10 ** (len(marks) - 1))))

add_marks(15)
print(marks)

def find_d(n):
    if n < 10:
        return n
    for i in range(len(marks)):
        if n <= marks[i]:
            start = marks[i - 1] + 1
            if (n - start) % i == 0:
                return 1 + ((n - start) // (i * (10 ** (i - 1))))
            elif (n - start) % i == i - 1:
                return (n - (start + 1)) % (i * 10) // i
            else:
                mod = (n - start) % i
                return ((n - start) % (i * (10 ** (i - mod))) // (i * (10 ** (i - mod - 1))))
answer = 1

for i in range(11):
    answer *= find_d(10 ** i)
print(answer)