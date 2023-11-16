import re

date = input('Enter the date: ')
print(date)

dateregex = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$')
mo = dateregex.search(date)

if mo:
    day = mo.group(1)
    month = mo.group(2)
    year = mo.group(3)
    
    if month in [4, 6, 9, 11] and day > 30:
        print('The date does not exist')
    elif month == 2:
        if year % 400 != 0 and (year % 4 != 0 or year % 100 == 0):
            if day > 28:
                print('The date does not exist')
        elif day > 29:
            print('The date does not exist')
    else:
        print('The date exists')
else:
    print('The date does not exist')
