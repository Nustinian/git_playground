palindromes = []
digits = [str(x) for x in range(10)]
for i in digits[1:]:
  for j in digits:
    for k in digits:
      palindromes.append(i + j + k + k + j + i)
      palindromes.append(i + j + k + j + i)
    palindromes.append(i + j + j + i)
    palindromes.append(i + j + i)
  palindromes.append(i + i)
  palindromes.append(i)
palindromes = sorted([int(x) for x in palindromes])
print(palindromes)
balindromes = [f"{x:b}" for x in palindromes]

sum = 0

for i in range(len(palindromes)):
  if balindromes[i] == balindromes[i][::-1]:
    sum += palindromes[i]

print(sum)
