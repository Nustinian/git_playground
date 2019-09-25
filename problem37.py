data = [int(num) for num in input().split()]

principal = data[0]
interest = data[1]/1200
months = data[2]
payment = 50000
payment_lower = 0
payment_upper = 100000

while principal >= 10 or principal <= -10:
    principal = data[0]
    for month in range(months):
        principal *= (1 + interest)
        principal -= payment
        if principal <= -10:
            payment_upper = payment
            payment = (payment + payment_lower) / 2
            break
    if principal >= 10:
        payment_lower = payment
        payment = (payment + payment_upper) / 2
