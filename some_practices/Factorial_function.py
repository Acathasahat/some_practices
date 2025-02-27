#definite a function for calculating factorial.
def factorial(num):
    num_factorial = None
    if num < 0 :
        return num_factorial
    elif num == 0 :
        num_factorial = 1
        return num_factorial
    elif num >= 1:
        for i in range(1,num+1):
            if num_factorial == None and i == 1:
                num_factorial = 1
            elif i > 1 :
                num_factorial = num_factorial * i
        return num_factorial

while True:
    n = input('Enter a positive integer: ')
    if n == 'done': break
    try:
        num = int(n)
    except ValueError:
        print(f'{n} is not a valid positive integer. Please try again: ')
        continue
    n_factorial = factorial(num)
    print(f'The factorial of {n} is {n_factorial}')