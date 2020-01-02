consonants = 'bcdfghjklmnprstvwxz'
vowels = 'aeiou'

first_line = [int(x) for x in input().split()]
counter, seed = first_line[0], first_line[1]
lengths = [int(x) for x in input().split()]

def step(seed):
    return (445 * seed + 700001) % 2097152

for length in lengths:
    word = ""
    while length > 0:
        seed = step(seed)
        if len(word) % 2 == 0:
            word += consonants[seed % 19]
        elif len(word) % 2 == 1:
            word += vowels[seed % 5]
        length -= 1
    print(word + " ")
