'''
Code for Project: Implement Your own Data Structures
'''
inventory = {'grapes': (10, 4.0)}

def add_item(k, val):
    inventory[k] = val
    print(f'Adding {k} to the inventory!')

#adding items using a method
add_item('banana', (2, 2.50))
add_item('pear',(4, 5.99))
add_item('mango', (5, 8,99))

print('All items in the inventory: ')
for i in inventory:
    print(f'Item: {i}, Quantity: {inventory[i][0]}, Price: {inventory[i][1]}')


#removing items
del inventory['pear']
print('removing \'pear\' from the inventory')

#updating the price of banana
li = list(inventory['banana'])
li[1] = 1.99
inventory['banana'] = li
print('Updated inventory: ')
for i in inventory:
    print(f'Item: {i}, Quantity: {inventory[i][0]}, Price: {inventory[i][1]}')


