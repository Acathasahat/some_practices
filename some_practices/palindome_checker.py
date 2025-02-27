#Check a phrase is a palindome
import re
def is_palindome(text):
    plain_text = re.sub(r'[^A-Za-z0-9\u4e00-\u9fff]','',text).lower()
    return plain_text.lower()== plain_text[::-1].lower()
while True:
    phrase = input('Enter a phrase to check: ')
    if phrase.lower() == 'done': 
        print('\nGoodbye!\n')
        break
    elif is_palindome(phrase):
        print(f'{phrase} is a palindome.\n')
    else:
        print(f'{phrase} is not a palindome\n')
    done_not=input('Do you wanna check more words?(Y/N): ')
    if done_not.lower() == 'y': continue
    else: 
        print('\nGoodbye!\n')
        break

        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
    