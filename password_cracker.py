# This is a basic code that cracks a password

import string
import random

password = input("Please input your password: ")

guess = ""          # our available parameter for cracking
character = list(string.printable)          # It gives all the possible characters in the available language
while guess != password:            # while our parameter is not equal to the password we are looking for
    guess = random.choices(character, k=len(password))      # This picks out random character from our character
    # variable and joins it together til it's the length of the password
    guess = "".join(guess)          # this will join all the character that the variable guess has given us
    print(guess)
print("Password: " + password)


# Note this code takes a lot of time to run, it goes over all the possible addition of characters just to find the

# password that has been entered
