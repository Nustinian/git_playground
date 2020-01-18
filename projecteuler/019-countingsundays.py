short_months = [4, 6, 9, 11]
dotw = 2 ##1 = monday
day = 1
month = 1
year = 1901
counter = 0

def happy_new_year():
    global year, month
    year += 1
    month = 1

def diet_next_month():
    global dotw, day, month, year, counter
    month += 1
    day = 1
    if dotw == 7:
        counter += 1
        print("{year}/{month}/{day} was a Sunday".format(year = year, month = month, day = day))
    if month == 13:
        happy_new_year()

def just_an_ordinary_day():
    global dotw, day, month, year
    dotw += 1
    if dotw == 8:
        dotw = 1
    day += 1
    if day >= 29:
        if month == 2 and year % 4 != 0:
            diet_next_month()
        elif month == 2:
            diet_next_month()
        elif month in short_months:
            if day == 31:
                diet_next_month()
        else:
            if day == 32:
                diet_next_month()

while year != 2001:
    just_an_ordinary_day()
print(counter)