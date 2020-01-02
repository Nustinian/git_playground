import string

def trim_string(string):
    return string[1:len(string) - 1]

counter = int(input())
for i in range(counter):
    input_string = input()
    no_punctuation = input_string.translate(str.maketrans('', '', string.punctuation))
    no_spaces = no_punctuation.replace(" ", "")
    lowercase = no_spaces.lower()
    answer = "Y"
    while len(lowercase) != 1 and len(lowercase) != 0:
        if lowercase[0] != lowercase[-1]:
        	answer = "N"
        lowercase = trim_string(lowercase)
    print(answer + " ")
