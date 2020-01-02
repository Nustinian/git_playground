counter = int(input())
for i in range(counter):
    cards = [card for card in input().split()]
    for index, card in enumerate(cards):
        if card in ["T", "J", "Q", "K"]:
            cards[index] = "10"
        elif card == "A":
            cards[index] = "11"
    cards = [int(card) for card in cards]
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    if sum(cards) > 21:
        print("Bust ")
    else:
        print(str(sum(cards)) + " ")
