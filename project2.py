#strong password detection 

import re

password=input('enter the password : ')

if len(password)>8:
    passwordRegex=re.compile(r'[a-zA-Z0-9]+')
    match=passwordRegex.search(password)
    if match!=None:
        print('strong password')
    else:
        print('weak password')
else:
    print("password is to short")
    

