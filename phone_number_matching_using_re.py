#import regular expression mofule
import re 

pattern='\d\d\d-\d\d\d-\d\d\d\d'
#if you want to give the different pattern uncomment below statement 
#pattern=input('Enter the pattern :')


#give the text in which you have to extract the phone number 
message=input("drop ur  message :")

phone_re=re.findall(pattern,message)

for num in phone_re:
    print("Here is your number : ",num)
print("The END")