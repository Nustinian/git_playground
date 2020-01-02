def luhn_checksum(list_number):
    checksum = 0
    for index, value in enumerate(list_number):
        if index % 2 == 1:
            checksum += value
        elif index % 2 == 0:
            temp = value * 2
            if temp >= 10:
                temp -= 9
            checksum += temp
    return checksum % 10 == 0

def swap_until_success(number):
    checksum = False
    for i in range(15):
        list_number = [int(x) for x in number]
        list_number[i], list_number[i + 1] = list_number[i + 1], list_number[i]
        if luhn_checksum(list_number):
            return list_number

def insert_until_success(number, index):
    for i in range(10):
        list_number = [x for x in number]
        list_number[index] = i
        list_number = [int(x) for x in list_number]
        if luhn_checksum(list_number):
            return list_number

counter = int(input())
for i in range(counter):
    number = input()
    if "?" in number:
        index = number.index("?")
        print("".join(map(str, insert_until_success(number, index))) + " ")
    else:
        print("".join(map(str, swap_until_success(number))) + " ")