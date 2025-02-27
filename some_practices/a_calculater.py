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
    
print('The operations:','\n','1.Add','\n','2.Subtract','\n','3.Multiply','\n','4.Divide')
choice = input('Please choose the operation:')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if choice == '1':
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == '2':
    print(num1,'-',num2,'=',subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,'=',multiply(num1,num2))
elif choice == '4':
    if num2 == 0:
        print('Cannot diveded by 0.')
       # quit()
    else:
        print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('invalid input.')