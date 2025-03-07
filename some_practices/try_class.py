class person_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return f'\nDeposited ${amount}, now the balance is ${self.balance}. '
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'\nWithdrowed ${amount}, now the balance is ${self.balance}'
        else:
            return f'\nInsufficient balance to withdrow ${amount}.'
    def check_balance(self):
        return f'\nThe balance is ${self.balance}.\n'
    
def operation(person,number):   
    if number == '2':
        deposit_amount = input('\nEnter the amount you deposit: ')
        try:
            deposit_num = float(deposit_amount)
            print(person.deposit(deposit_num))
        except ValueError:
            print('Please enter a valid number.\n ')
                    
    elif number == '3':
        withdrow_amount = input('\nEnter the amount you withdrow: ')
        try:
            withdraw_num = float(withdrow_amount)
            print(person.withdraw(withdraw_num))
        
        except ValueError:
            print('Please enter a valid number.\n ')
            
        
    elif number == '4':
        print(person.check_balance())
        
    elif number == '5':
        print(f'\nYour account: {person.name}\n Your balance: {person.balance} \nThanks and Goodbye!\n')
        return False
    else:
        print('Please enter a valid number of the operations.\n')
        

user_input = ''
person = None
while user_input.lower() != 'done':
    print('\nWelcome to our bank. Please choose your operation:')
    user_input = input( '1(Create an account\n2(Deposit)\n3(Withdrow)\n4(Check your balance)\n5(Log out)): \n')
    if user_input == '1':
        print('Hello, you need to create your own account with your initial balance.\n')
        user_name = input('Please enter your name: ')
        initial_balance = input('Please enter your initial balance: ')
        try:
            person = person_account(user_name,float(initial_balance))
            print(f'\nAccount created for {user_name} with balance ${initial_balance}.\n')
        except ValueError:
            print('Please enter a valide number.\n')
    elif person:
        if operation(person,user_input) == False: break
    else:
        print('Please create an account first.\n')
    
        
    