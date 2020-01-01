counter = int(input())
for i in range(counter):
    nums = [int(x) for x in input().split()]
    answer = 0
    for num in nums:
        answer += num ** 2
    print(str(answer) + " ")
