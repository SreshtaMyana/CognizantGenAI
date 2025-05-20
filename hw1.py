'''
Code for homework 1 of the externship
'''
#task 1 code
name = 'Samuel'
age = '27'
height = '5.4'
str = f'Task 1 Output: Hello!, My name is {name}, I turn {age} this year, and I am officially {height} feet tall!'
print(str+'/n')

#task 2 code
num1 = 78
num2 = 98
print('Task 2 operations:')
print(f'adding num1 and num2: {num1+num2}\n') #addition
print(f'subtracting num2 from num1: {num1-num2}\n') #subtraction
print(f'multiplying num1 and num2: {num1*num2}\n') #multiplication
print(f'dividing num1 by num2: {num2/num1}\n') #division

#task 3
us_inp = int(input('for task 3, enter your number:')) #takes input from user and converts to integer
if us_inp > 0: #positive number
    print("This number is positive. Awesome!")
elif us_inp < 0: #negative number
    print("This number is negative. Better luck next time!")
else: #zero
    print("Zero it is. A perfect balance!")