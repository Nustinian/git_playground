suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
counter = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
    suit = num // 13
    rank = num % 13
    print(ranks[rank] + "-of-" + suits[suit] + " ")