import sys
import random

'''
def randfunc():
    first_number = input('enter starting number')
    second_number = input('enter ending number')
    rand = random.randint(int(first_number), int(second_number))
    while (rand == 76):
        print(f'you have won as your number is {rand}')
        break
    else:
        print('you lose try again')
    print(rand)


randfunc()
'''


def random_func():
    rand = random.randint(1, 10)
    guess = input('guess the number between 1 to 10 : ')
    while(guess == rand):
        print('you have won....')
        break
    else:
        print(f'try again {guess} is not the number we are looking for')


random_func()
