counter = int(input())

originals = [float(x) for x in input().split()]
smoothed = [originals[0]]
for i in range(counter - 2):
    sum = originals[i] + originals[i + 1] + originals[i + 2]
    average = sum / 3
    smoothed.append(average)
smoothed.append(originals[-1])
for num in smoothed:
    print(str(num) + " ")