num = int(input('enter your starting number: '))
if num > 0:
    while num != 0:
        print(str(num), end=' ')
        num -= 1
    print('Blast off!')
else:
    print('enter a number greater than zero.')