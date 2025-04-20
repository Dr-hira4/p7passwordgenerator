#project 7 : password generator

import random
import string

def generated_password(length=12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

#users inputs
length = int(input("enter the length of your desired password: "))

password = generated_password(length)
print("Your desired password" , password)
