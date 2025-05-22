'''
Code for Project: About Menu
'''
#factorial method
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

#fibonacci method   
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

st = 'Welcome! choose what you would like to see by entering the number corresponding to each action:\n' \
    '1: Fibonacci ' \
    '2: Factorial ' \
    '3: Exit  '

while True:
    in_pu = int(input(st))
    if in_pu == 1 or in_pu == 2:
        num = int(input('Enter your number: '))
        if in_pu == 1:
            print(f'The Fibonacci of {num} is {fibonacci(num)}!')
        elif in_pu == 2:
            if str(num)[-1] == '1':
                pr = 'st'
            elif str(num)[-1] == '2':
                pr = 'nd'
            elif str(num)[-1] == '3':
                pr = 'rd'
            else:
                pr = 'th'
            print(f'The {num}{pr} Factorial is {factorial(num)}!')
    elif in_pu == 3:
        print(f'Exiting the program! Thank you!')
        break
    else:
        print('Unidentified action')
