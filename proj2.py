'''
Code for Project: Number Guessing Game
'''
import random

guess_dis = random.randint(1, 100)
tries = 1
while tries < 11:
    us_inp = int(input('Guess the number (between 1 and 100): '))
    if us_inp > guess_dis:
        print("Too high! Try again.")
    elif us_inp > guess_dis:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed it!")
        print(f'Guessed at try {tries}')
        break
    tries += 1

if tries == 11:
    print("Game over! Better luck next time!")