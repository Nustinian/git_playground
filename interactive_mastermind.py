import random

def check_correct(guess, answer):
    number_correct = 0
    correct_positions = []
    for i in range(4):
        if guess[i] == answer[i]:
            number_correct += 1
            correct_positions.append(i)
    return number_correct, correct_positions

def check_misses(guess, answer, correct_positions):
    near_misses = 0
    check_these_positions = [i for i in range(4) if i not in correct_positions]
    also_added = []
    for i in check_these_positions:
        for j in check_these_positions:
            if j not in also_added:
                if guess[i] == answer[j]:
                    near_misses += 1
                    also_added.append(j)
                    break
    return near_misses

def get_guess(prompt="\nWhat will be your next guess?\n"):
    try_again_message = "Please enter a number between 0000 and 9999\n"
    while True:
        try:
            guess = input(prompt)
        except ValueError:
            print(try_again_message)
            continue
        try:
            if int(guess) < 0 or int(guess) > 9999 or len(guess) != 4:
                print(try_again_message)
                continue
        except ValueError:
            print(try_again_message)
            continue
        else:
            return guess

def another_round():
    print("\nYour guesses so far:")
    for i in range(len(guess_history)):
        print("" + guess_history[i] + " " + result_history[i])
    guess = input("\nWhat will be your next guess?\n")
    number_correct, correct_positions = check_correct(guess, answer)
    near_misses = check_misses(guess, answer, correct_positions)
    guess_history.append(guess)
    result_history.append(str(number_correct) + "-" + str(near_misses))
    return guess

def report_results():
    if result_history[-1][0] == "4":
        print("That's right!\n")
        if tries == 1:
            print("\nYou probably should have spent that luck on a lottery ticket...")
    else:
        print("\n" + result_history[-1][0] + " Correct\n" + result_history[-1][2] + " Wrong Position")


print("\nLet's play Mastermind!")

answer = "1234"#f'{random.randrange(0, 10**4):04}'
guess_history = []
result_history = []
guess = get_guess("\nGo ahead and make your first guess. Good luck!\n")
tries = 1
number_correct, correct_positions = check_correct(guess, answer)
near_misses = check_misses(guess, answer, correct_positions)
guess_history.append(guess)
result_history.append(str(number_correct) + "-" + str(near_misses))
report_results()
while guess != answer:
    tries += 1
    guess = another_round()
    report_results()