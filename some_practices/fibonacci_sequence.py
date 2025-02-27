#Generate the Fibonacci sequence up to a given number.
#f(0) = 0 and f(1) = 1
input(f'This code is used to generate the Fibonacci sequence up to the given number. Press the Enter to start_')
def infinit_range(start):
    while True:
        yield start
        start += 1
while True:
    f_sequence =[0,1]
    n = input('\nPlease enter a Fibonacci (or \'done\' if you finished): ')
    if n.lower() == 'done': break
    try:
        n = int(n)
    except ValueError:
        input(f'{n} is not a valid number. please try again_ \n')
        continue
    if n == 0:
        print(f'the Fibonacci sequence is: {f_sequence[0:1]} \n')
    elif n >= 1:
        for i in infinit_range(2):
            a = i - 2
            b = i - 1
            f = f_sequence[a] + f_sequence[b]
            f_sequence.append(f)
            #print(f_sequence)
            if n == 1:
                print(f'The Fibonacci sequence is: {[0,1]} or {f_sequence} \n')
                break
            elif n != 1 and n == f :
                print(f'The Fibonacci sequence is: {f_sequence} \n')
                break
            elif n != 1 and n < f:
                print(f'The Fibonacci sequence is: {f_sequence}. \n{n} is not a fibonacci number.')
                break
            
    answer = input('Do you want try more Fibonacci? (Y/N) ')
    if answer.lower() == 'y': continue
    else: 
        input('Goodbye! Please press the Enter to exit.')
        break
    