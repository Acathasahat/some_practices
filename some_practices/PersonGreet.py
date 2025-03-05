class Person:
    def __init__(self,name,age): #__init__是特殊方法，当创建类实例时自动调用。这个方法接受两个参数self(指向类实例本身的引用)和name、age(用于初始化对象的属性)
        self.name = name#将传入的name参数赋值给name属性
        self.age = age#将传入的age参数赋值给age属性
        
    def greet(self): #greet是类Person中的一个方法，只接受self参数并返回一句问候语
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
while True:
    name = input('What\'s your name? ' )
    if name.lower() == 'done': 
        break
    while True:
        age = input('How old are you? ')
        try:
            age_num = int(age)
            break
        except ValueError:
            print(f'\n{age} is not a valid age number.')
            continue
        

    person = Person(name,age_num)
    print(person.greet())
    
    print(f"\nIf you finished, please enter 'done'.")
print('\nGoodbye!\n')




