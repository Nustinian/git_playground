words = input().split()
seen_once = []
seen_twice = []
for word in words:
    if word in seen_once:
        if word not in seen_twice:
            seen_twice.append(word)
    else:
        seen_once.append(word)
seen_twice.sort()
for word in seen_twice:
    print(word + " ")