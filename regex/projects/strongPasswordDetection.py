import re

def is_strong_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[._@#!$%&*])[a-zA-Z0-9._@#!$%&*]{8,}$'
    return bool(re.search(pattern, password))

password = input('Enter your password: ')

if is_strong_password(password):
    print('Stronk')
else:
    print('Weak')
