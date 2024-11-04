import re
from getpass4 import getpass

def is_strong_password(password):
    # m3gakr4nus called it 'regex on god mode' and I agree.
    ''' The (?=.*[<some-pattern>]) syntax means that pattern should be present
    and the next such syntax also must meet, altho not in the same order.
    The pattern expects small alphabet, big alphabet, number, any symbol from the set
    ALSO it should be 8 or more characters as defined in the last one'''
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[._@#!$%&*])[a-zA-Z0-9._@#!$%&*]{8,}$'
    return bool(re.search(pattern, password))

password = getpass('Enter your password: ')

if is_strong_password(password):
    print('Stronk')
else:
    print('Weakling')
