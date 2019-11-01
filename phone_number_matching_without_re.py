#create a fucntion to check pattern is matchs with XXX-XXX-XXXX

def isphonenumber(text):
    if len(text)!=12:
        return False
    if not text[0:3].isdecimal() :
        return False
    if text[3]!='-':
        return False
    if not text[4:7].isdecimal():
        return False
    if text[7]!='-':
        return False
    if not text[8:12].isdecimal():
        return False
    return True

message=input("drop ur  message: ")
for i in range(len(message)):
    match=message[i:i+12]
    if isphonenumber(match):
        print("Here is your number :" ,match)
print("The END")