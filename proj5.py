import turtle

#factorial method
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

#fibonacci method   
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
'''
def draw_fractal_tree(turtle, branch_length, angle, depth):
    if depth == 0:
        return
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_fractal_tree(turtle, branch_length * 0.7, angle, depth - 1)
    turtle.right(2 * angle)
    draw_fractal_tree(turtle, branch_length * 0.7, angle, depth - 1)
    turtle.left(angle)
    turtle.backward(branch_length)

screen = turtle.Screen()
tree_turtle = turtle.Turtle()
tree_turtle.speed(0)
tree_turtle.left(90)
draw_fractal_tree(tree_turtle, 100, 30, 7)
screen.mainloop()
'''

st = 'Welcome! choose what you would like to see by entering the number corresponding to each action:\n' \
    '1: Fibonacci\n' \
    '2: Factorial\n' \
    '3: A fractal tree\n'
in_pu = input(st)
num = 9
nu_m = 9
if in_pu == '1':
    print(f'The Fibonacci of {num} is {fibonacci(num)}!')
elif in_pu == '2':
    print(f'The Factorial of {nu_m} is {factorial(nu_m)}!')
elif in_pu == '3':
    print(f'Here is the diagram of the fractal tree!')
