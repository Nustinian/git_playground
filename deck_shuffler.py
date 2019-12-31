deck = [suit + rank for suit in "CDHS" for rank in "A23456789TJQK"]
randoms = [int(x) % 52 for x in input().split()]

for i in range(52):
    deck[i], deck[randoms[i]] = deck[randoms[i]], deck[i]
    
for i in range(52):
    print(deck[i] + " ")