'''
code for homework:  About Parameters of Functions
'''
#task 1
def greet_user(name):
    return f'Hello {name}! Nice to meet you.'

def add_numbers(n1, n2):
    return f'The sum of {n1} and {n2} is {n1+n2}!'

n = 'Jacob'
n1, n2 = 34, 90
print(greet_user(n) + add_numbers(n1, n2))

#task 2
def descibe_pet(pet_name, animal_type):
    return f'My pet {pet_name} is an adorable {animal_type}'

#task 3
def make_sandwich(*args):
    return f'The ingredients of your sandwich are: {', '.join(args)}'

print(make_sandwich('lettuce', 'onions', 'potato', 'bread'))

#task 4
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = 5
print(f'The factorial for {num} is {factorial(num)}!')

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
f = 6

pr = ''

if str(f)[-1] == '1':
    pr = 'st'
elif str(f)[-1] == '2':
    pr = 'nd'
elif str(f)[-1] == '3':
    pr = 'rd'
else:
    pr = 'th'

print(f'The {f}{pr} fibonacci is {fibonacci(f)}')
