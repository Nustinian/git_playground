import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def format_output(word):
    output = ""
    i = 1
    for definition in data[word]:
        output += "Definition {i}: ".format(i = i) + definition + "\n"
        i += 1
    return output

def define(word):
    word = word.lower()
    if word in data:
        return format_output(word)
    else:
        suggestion = get_close_matches(word, data.keys(), 1, 0.8)
        if len(suggestion) == 1:
            user_input = input("Did you mean {suggestion}? Y or N: ".format(suggestion = suggestion)).lower()
            while True:
                if user_input == "y":
                    return format_output(suggestion[0])
                elif user_input == "n":
                    return "Sorry, your word is not in the dictionary."
                else:
                    user_input = input("Please input Y or N: ")
        return "That word is not in the dictionary."

word = input("Enter word: ")

print(define(word))