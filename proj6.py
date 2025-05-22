'''
Code for Project: Calculator with Exception Handling
'''

while True:
    try:
        act = int(input('Welcome to the Error-Free Calculator! ' \
        'Choose an operation: ' \
        '1. Addition ' \
        '2. Subtraction ' \
        '3. Multiplication ' \
        '4. Division ' \
        '5. Exit '))

        li = [1,2,3,4]
        if act in li: #writing this to find if any number is part of action, if it says exit, don't take n1 and n2
            n1 = int(input('Enter your first number!: '))
            n2 = int(input('Enter your second number!: '))
            if act == 1:
                print(f'Adding {n1} and {n2} gives us {n1+n2}!')
            elif act == 2:
                print(f'Subtracting {n1} from {n2} gives us {n2-n1}!')
            elif act == 3:
                print(f'Multiplying {n1} and {n2} gives us {n1*n2}!')
            elif act == 4:
                print(f'Dividing {n1} by {n2} gives us {n1/n2}!')
        elif act == 5:
            print('Thank you and Happy calculating!')
            break    
        else:
            print('Please choose one of the options')
    except ZeroDivisionError:
        print('Oops! You can\'t divide anything by zero!')
    except ValueError:
        print('Please enter the right numbers')