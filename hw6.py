'''
Code for Assignment: Check your Knowledge on Errors
'''
#task 1
f_n = int(input('Enter your number: '))
try:
    print(f'Dividing 100 by {f_n} gives us {100/f_n}')
except ZeroDivisionError:
    print(f'Can\'t divide a number by zero!')
except ValueError:
    print('please only enter integers!')

#task 2
my_list = [0,2,45,'water']
my_dictionary = {'water': 'bottle', 'zinky': 'zoop boop'}
try:
    print(my_list[20]) #raises indexerror
except IndexError:
    print('You raised an index error! You can\'t access an element that isn\'t in the list!')

try:
    print(my_dictionary['zup']) #raises keyerror
except KeyError:
    print('You raised a key error! You can\'t access a value from a dictionary with a key that isn\'t in the dictionary!')

try:
    print('water' + 234) #raises valueerror
except TypeError:
    print('You raised a value error! can\'t concatenate a string and an int or add up a string and an int!')

#task 3
try:
    n1 = int(input('Enter your first number: '))
    n2 = int(input('Enter your second number: '))
    val = n1/n2
except ZeroDivisionError:
    print(f'Can\'t divide a number by zero!')
except ValueError:
    print('please only enter integers!')
except:
    print('An issue occured')
else:
    print(f'Dividing {n1} by {n2} gives us {n1/n2}')
finally:
    print('Task finished! Happy division!')
