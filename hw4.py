'''
code for homework 4: Hands on Python Data Structures
'''
#task 1
fruitz = ['apple', 'banana', 'orange', 'grapes', 'papaya']
print(f'fruits list: {fruitz}')
fruitz.append('fig')
print(f'adding fig to fruits: {fruitz}')
fruitz.remove('apple')
print(f'removing apple from fruits: {fruitz}')
print(f'reversing fruits: {fruitz[::-1]}')

#task 2
dat = {'name':'Santhi', 'age': 19, 'city': 'Delhi'}
dat['favorite color'] = 'Black'
dat['city'] = 'Paris'

dat_keys = ''
dat_values = ''
for i in dat:
    dat_keys += str(i) + ' ,'
for j in dat:
    dat_values += str(dat[j]) + ' ,'

print(f'keys: {dat_keys}')
print(f'values: {dat_values}')

#task 3
fav_stuff = ('Avatar', 'Shake it off!', 'The Da Vinci Code')
print(f'My favorite items: {fav_stuff}')

try:
    fav_stuff[0] = 'Tarzan'
except TypeError:
    print("Oops! Tuples cannot be changed.")
    
print(f'length of fav_stuff: {len(fav_stuff)}')