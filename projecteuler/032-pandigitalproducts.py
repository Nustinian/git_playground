def is_pandigital(mynum):
  listnum = list(set([i for i in mynum]))
  return all(x in [i for i in str(123456789)] for x in listnum) and len(listnum) == 9

pandigital_products = []

for i in range(2000):
  for j in range(2000):
    product = i * j
    mynum = str(i) + str(j) + str(product)
    if len(mynum) > 9:
      break    
    if len(mynum) == 9:
      if is_pandigital(mynum):
        pandigital_products.append(product)
        print(i, " * ", j, " = ", product)

print(set(pandigital_products))
print(sum(set(pandigital_products))) 
