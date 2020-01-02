primes_list = [True for i in range(3000001)]
p = 2
while p <= int(3000000 ** 0.5):
  if primes_list[p] == True:
    for i in range(p*p, 3000001, p):
        primes_list[i] = False
  p += 1
counter = int(input())
nums = [int(x) for x in input().split()]
answer = ""
for num in nums:
    index = 0
    for i in range(2, len(primes_list)):
        if primes_list[i] == True:
            index += 1
            if index == num:
                answer += str(i) + " "
print(answer)