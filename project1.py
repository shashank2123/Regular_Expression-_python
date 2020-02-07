#Phone Nummber and email extractor 
import re
import pyperclip


#get the test from clipboard
text=pyperclip.paste()

phoneRegex=re.compile(r'(\+)?(\d{2,3})?(\.|\s|-)?(\d\d\d)(\.|\s|-)?(\d\d\d)(\.|\s|-)?(\d\d\d\d)')
phoneNum=phoneRegex.findall(text)

emailRegex=re.compile(r'''[A-Za-z0-9%+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}''')
emails=emailRegex.findall(text)

matches=[]
for w in phoneNum:
    out_text=''.join(list(w))
    matches.append(out_text)
    
for t in emails:
    matches.append(t)

text_output='\n'.join(matches)

if len(text_output)>0:
    pyperclip.copy(text_output)
else:
    pyperclip.copy("No Match Found")