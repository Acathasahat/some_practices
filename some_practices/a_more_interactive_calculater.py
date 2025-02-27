def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b 
def divide(a,b):
    if b == 0:
        return print('cannot devided by 0.')
    else:
        return a / b

while True:
    print('\n','Operations (1-5):')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    print('5.Exit','\n')
    c_list = ['1','2','3','4']
    
    choice = input('Choose one operation: ')
    if choice in c_list:   
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print('Invalid number')
            continue
        if choice == '1':
            print(num1,'+',num2,'=',add(num1,num2),'\n')
        elif choice == '2':
            print(num1,'-',num2,'=',subtract(num1,num2),'\n')
        elif choice == '3':
            print(num1,'*',num2,'=',multiply(num1,num2),'\n')
        elif choice == '4':
            print(num1,'/',num2,'=',divide(num1,num2),'\n')
    elif choice == '5':
        break
    else:
        print('Please choose an operation showed! ','\n')
        continue
           
    choice2 = input('Do you want to do more operation? (y/n):' )
    if choice2 != 'y':
        break
        
        
    