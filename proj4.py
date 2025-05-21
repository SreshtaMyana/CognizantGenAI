'''
Code for Project: Implement Your own Data Structures
'''
inventory = {}
inventory['banana'] = (2, 2.50)
inventory['pear'] = (4, 5.99)
inventory['mango'] = (5, 8,99)
inventory.remove('pear')

#updating the price of banana
li = list(inventory['banana'])
li[1] = 1.99
inventory['banana'] = li
print('Updated inventory:')
