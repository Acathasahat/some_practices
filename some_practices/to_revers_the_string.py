#To reverse an entered string
input('This code is used to reverse the string you entered.')
while True:
    string = input(f'Enter a string (or \'done\' if you finished): ')
    if string.lower() == 'done': 
        input('\nGoodbye! Press the Enter to exit.')
        break
    reversed_str = string[::-1]
    print(f'The reverse of {string} is: {reversed_str}\n')

        

    