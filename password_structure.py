from password_creator import Password
import re
#l=int(input("input password length : "))
print("Enter s for special symbols \nEnter u for Upper case Character\nEnter l for lower case")
print("Enter d for digits \nCombinations can also be entered\n")
ch=str(input( "Enter characters : "))
l=int(input("Input password length : "))
if set(ch).issubset("suld"):
    password = Password(ch, l)
    password.set_the_charset()
    password.generate_password()
    print("the random password is : ", password.get_password())
else:
    print("You entered wrong characters \nPlease enter characters between 's' 'u' 'l' 'd' \n ")