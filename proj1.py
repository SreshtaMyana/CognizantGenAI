'''
Code for Project: Eligible Elector
'''
age = int(input("How old are you? ")) #take input from user
if age >= 18: #if age is greater than or equal to 18, do this
    print('Congrats! You are eligible to vote!\n')
else: #if age is less than 18, do this
    print(f'You still have {18 - age} years to become eligible to vote!')