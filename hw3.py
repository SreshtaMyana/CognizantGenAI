'''
Code for homework 3: Exploring String Methods
'''
#task 1
st_r = "Python is amazing!"
f_w = st_r[:6]
print(f'First word: {f_w}')
word_amaz = st_r[-8:]
print(f'amazing word: {word_amaz}')
rev_str = st_r[::-1]
print(f'Reversed String: {rev_str}')

#task 2
h_w = "hello, python world!"
print(f'removing whitespaces from h_w: {h_w.strip()}')
print(f'Capitalizing the first letter in h_w: {h_w[0].capitalize() + h_w[1:]}')
print(f'replacing world with universe: {h_w.replace('world', 'universe')}')
print(f'converting all letters to uppercase: {h_w.upper()}')

#task 3
us_imp = input('Enter a word or string: ')
if us_imp == us_imp[::-1]:
    print(f'Your input \'{us_imp}\' is a palindrome!')
else:
    print(f'Your input \'{us_imp}\' is not a palindrome!')