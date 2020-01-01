with open("words.txt") as words:
    words = [sorted(line.rstrip('\n')) for line in open("words.txt")]

counter = int(input())
for i in range(counter):
    term = sorted(input())
    anagrams = 0
    for word in words:
        if term == word:
            anagrams += 1
    print(anagrams - 1, " ")