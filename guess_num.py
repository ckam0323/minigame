#!/usr/local/bin/python3
# guess figure in 1-100
import random
time = 0        # inital times
num = (random.randint(1,100))   # from 1 - 100 get random number

while time < 7:     # Seven chances
    time += 1
    unum = int(input("guess: "))
    if unum < num :
        print('\033[33;1mGuess small\033[0m')
    elif unum > num:
        print('\033[33;1mGuess big\033[0m')
    else :
        print('\033[32;1mGuess right\033[0m')
        break
else:
    # If player can't guess right,print the answer in the screen
    print('Answer is: \033[31;1m%s\033[0m' % num)
    print('Total \033[31;1m%s\033[0m times' % time)