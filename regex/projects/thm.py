'''
A program which takes an IP address from the clipboard and converts it into the THM notation.
Eg. 10.10.192.132 will be converted to http://10-10-192-132.p.thmlabs.com.

Note: Doesn't work for ports.
'''

import re
import pyperclip

postStr = '.p.thmlabs.com'
proto = 'http://'

def actual_work(str):
    cleansed = ip.replace('.', '-')
    output = proto + cleansed + postStr
    pyperclip.copy(output)
    print('Done: ' + output)

def ip_sanity(ip):
    subnet_reg = r'\d{1,3}'
    result = re.findall(subnet_reg, ip)
            
    # Check if there are exactly 4 parts and each part is a valid subnet (0-255)
    if len(result) == 4 and all(0 <= int(part) < 256 for part in result):
        return True
    else:
        print("Warning: Not a correct IP.")
        return False
        

ip_pattern = r'^(\d{1,3}.){3}\d{1,3}$'

ip = pyperclip.paste()

if re.search(ip_pattern, ip):
    ip_sanity(ip)
    actual_work(ip)
else:
    print('Not even an IP.')
