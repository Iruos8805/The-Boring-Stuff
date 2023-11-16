def collatz(number):
    if number%2 == 0:
        value = number // 2
        return  value
    else:
        value = 3*number+1
        return value

print('Enter an integer:')
try:
    number = int(input())
    while True:
        value = collatz(number)
        print('value is ' + str(value))
        number = value
        print('number is' + str(number))
        if number == 1:
            break
except ValueError :
    print('Please enter an integer')