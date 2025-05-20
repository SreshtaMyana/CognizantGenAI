'''
Project: Eligible Elector
'''
age = int(input("How old are you? "))
if age >= 18:
    print('Congrats! You are eligible to vote!\n')
else:
    print(f'You still have {18 - age} years to become eligible to vote!')