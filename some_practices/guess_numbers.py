#猜数字游戏的程序，保证良好的交互性
import random
print('Welcom to play the Number Guess Game.')
print('First the computer will give a random number in 1 to 100.')
print('You could try your best to guess it.')
print('If during the playtime you do not want to play, please enter quit.')
answer = input('Are you ready to guess now?')
print('\n')
while True:
    attempts = 0
    the_num_to_guess = random.randint(1,101)
    print('I have got a number.')
    while True:
        guess_num_str = input('Please have a guess now: ')
        if lower(guess_num_str) == 'quit':
            exit()
        try:
            guess_num =int(guess_num_str)
        except ValueError:
            print(guess_num_str,'is not a valid number. Please enter a valid whole number.','\n')
            continue
        attempts += 1
        if guess_num <the_num_to_guess:
            print('The number is bigger than',guess_num,'\n')
            continue
        elif guess_num > the_num_to_guess:
            print('The number is smaller than',guess_num,'\n')
            continue
        else:
            print('Congradulations! You got acuratly the number by', attempts,'times guesses.','\n')
            break
            
    print('Game is over now')
    choice = input('Do you want to guess one more time?(y/n) ')
    if lowe(choice) != 'y':
        print('Goodbye!')
        exit()
        
        
