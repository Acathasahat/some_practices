#to check whether a number is a prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2,round(number**0.5)+1):
        if number % i == 0: 
            return False
    return True #for 循环都没找到因数时才返回True
while True: 
    number_string = input('Enter a positive integer to check: ')
    if number_string.lower() == 'done': break
    try: 
        number = int(number_string)
    except ValueError:
        print(f'{number} is not a valid positive integer.')
        continue
    if is_prime(number):
        print(f'{number} is a prime.')
    else:
        print(f'{number} is not a prime.')
    
    question = input('Do you wanna check more numbers? (Y/N) ')
    if question.lower() == 'y': continue
    else: break
