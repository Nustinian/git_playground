digit_bank = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen_bank = ["cake", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_bank = ["cake", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def is_teen(str_number):
    if int(str_number[-2:]) < 20 and int(str_number[-2:]) > 10:
        return True

def is_single(str_number):
    if int(str_number[-2:]) < 10 and int(str_number[-2:]) > 0:
        return True

def translate_to_words(number):
    str_number = str(number)
    if len(str_number) == 3:
        a = int(str_number[0])
        b = int(str_number[1])
        c = int(str_number[2])
        if number % 100 == 0:
            return digit_bank[a] + " hundred"
        elif number % 10 == 0:
            return digit_bank[a] + " hundred and " + tens_bank[b]
        else:
            if is_teen(str_number):
                return digit_bank[a] + " hundred and " + teen_bank[c]
            elif is_single(str_number):
                return digit_bank[a] + " hundred and " + digit_bank[c]
            else:
                return digit_bank[a] + " hundred and " + tens_bank[b] + " " + digit_bank[c]
    elif len(str_number) == 2:
        b = int(str_number[0])
        c = int(str_number[1])
        if number % 10 == 0:
            return tens_bank[b]
        else:
            if is_teen(str_number):
                return teen_bank[c]
            else:
                return tens_bank[b] + " " + digit_bank[c]
    elif number < 10:
        return digit_bank[number]
    else:
        return "one thousand"

letters = ""
for i in range(1, 1001):
    letters += "".join(translate_to_words(i).split())
print(len(letters))

