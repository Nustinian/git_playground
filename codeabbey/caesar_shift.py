first_line = [int(x) for x in input().split()]
counter = first_line[0]
k = first_line[1]
for i in range(counter):
    message = input()
    new_message = []
    for letter in message:
        if letter == " ":
            new_message.append(letter)
        elif letter == ".":
            new_message.append(". ")
        else:
            ascii_code = ord(letter) - k
            if ascii_code < 65:
                ascii_code += 26
            new_message.append(chr(ascii_code))
    print("".join(new_message))
