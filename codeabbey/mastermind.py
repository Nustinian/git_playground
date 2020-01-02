def check_correct(guess, answer):
    number_correct = 0
    correct_numbers = []
    for i in range(4):
        if guess[i] == answer[i]:
            number_correct += 1
            correct_numbers.append(guess[i])
    return number_correct, correct_numbers

def check_misses(guess, answer, correct_numbers):
    near_misses = 0
    misses = [number for number in guess if number not in correct_numbers]
    for number in misses:
        if number in answer:
            near_misses += 1
    return near_misses

answer = input().split()[0]
nums = [x for x in input().split()]

for guess in nums:
    number_correct, correct_numbers = check_correct(guess, answer)
    near_misses = check_misses(guess, answer, correct_numbers)
    print(str(number_correct) + "-" + str(near_misses) + " ")