while True:
    try:
        guess = input("Please give me a four digit number\n")
    except ValueError:
        print("What?\n")
        continue
    try:
        if int(guess) < 0 or int(guess) > 9999 or len(guess) != 4:
            print("Try again yo\n")
            continue
    except ValueError:
        print("that's not a number yo\n")
        continue
    else:
        break
print("the number" + guess + "is acceptable\n")