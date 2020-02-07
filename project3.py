#Replicate the strip() using re

import re 

def restrip(text):
    stripRegex=re.compile(r'[a-zA-Z0-9@!#$%^&*\(\)\\\/<>\?\:\"\']+')
    matches=stripRegex.findall(text)
    out_text=' '.join(matches)
    return(out_text)
    
text=input("the text :")

out=restrip(text)

print(out)