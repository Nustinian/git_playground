counter = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
    data = int(num) % 0x100000000
    bits = format(data, 'b')
    print(str(bits.count('1')) + " ")