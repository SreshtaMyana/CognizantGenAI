'''
Code for 
'''
pass_wrd = input('enter a password: ')
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0
unknown_chars = 0
special_chars = '#@$'
if len(pass_wrd) < 8:
    print('Your password must contain at least 8 character')
else:
    for i in pass_wrd:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        elif i.isdigit():
            digit_count += 1
        elif i in special_chars:
            special_count += 1
        else: #gets triggered if a char is not part of special chars, like '.', '?', '['
            unknown_chars += 1

    if upper_count == 0:
        print('Your password must contain atleast one uppercase letter')
    elif lower_count == 0:
        print('Your password must contain atleast one lowercase letter')
    elif digit_count == 0:
        print('Your password must contain atleast one digit/number')
    elif special_count == 0:
        print('Your password must contain atleast one special character like #, @, or $')
    elif unknown_chars > 0:
        print('Can\'t have any other characters!')
    else:
        print('That\'s a strong password!')
            
