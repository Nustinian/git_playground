target = 20
coins = [1, 2, 5, 10, 20]
ways = [1] + [0] * target

for coin in coins:
  for i in range(coin, target + 1):
    ways[i] += ways[i - coin]
    print(ways, i, coin)


