firstmark = 1 * 9
secondmark = firstmark + 2 * 90
thirdmark = secondmark + 3 * 900
fourthmark = thirdmark + 4 * 9000
fifthmark = fourthmark + 5 * 90000
sixthmark = fifthmark + 6 * 900000


def find_d(n):
    if n < firstmark + 1:
        return n
    if n < secondmark + 1:
        if n % 2 == 0:
            return 1 + (n - 10) // 20
        return ((n - 11) % 20) // 2
    if n < thirdmark + 1:
        if (n - 190) % 3 == 0:
            return 1 + ((n - 190) // 300)
        if (n - 190) % 3 == 1:
            return ((n - 190) % 300) // 30
        if (n - 190) % 3 == 2:
            return ((n - 191) % 30) // 3
    if n < fourthmark + 1:
        if (n - 2890) % 4 == 0:
            return 1 + ((n - 2890) // 4000)
        if (n - 2890) % 4 == 1:
            return ((n - 2890) % 4000) // 400
        if (n - 2890) % 4 == 2:
            return ((n - 2890) % 400) // 40
        if (n - 2890) % 4 == 3:
            return ((n - 2891) % 40) // 4
    if n < fifthmark + 1:
        if (n - 38890) % 5 == 0:
            return 1 + ((n - 38890) // 50000)
        if (n - 38890) % 5 == 1:
            return ((n - 38890) % 50000) // 5000
        if (n - 38890) % 5 == 2:
            return ((n - 38890) % 5000) // 500
        if (n - 38890) % 5 == 3:
            return ((n - 38890) % 500) // 50
        if (n - 38890) % 5 == 4:
            return ((n - 38891) % 50) // 5
    if n < sixthmark + 1:
        if (n - 488890) % 6 == 0:
            return 1 + ((n - 488890) // 600000)
        if (n - 488890) % 6 == 1:
            return ((n - 488890) % 600000) // 60000
        if (n - 488890) % 6 == 2:
            return ((n - 488890) % 60000) // 6000
        if (n - 488890) % 6 == 3:
            return ((n - 488890) % 6000) // 600
        if (n - 488890) % 6 == 4:
            return ((n - 488890) % 600) // 60
        if (n - 488890) % 6 == 5:
            return ((n - 488891) % 60) // 6


answer = 1

for i in range(7):
    answer *= find_d(10 ** i)

print(answer)
