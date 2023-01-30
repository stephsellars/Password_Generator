"""This program is simply to create a unique 16-character password for any site one may need it for. 
Once the script is executable, it can be added to the desktop for easy access. Running the script will
create said password and log it into the file 'saved-passwords.txt' with the site it is for, once inputted
by the user. Just be sure to have both files in the same directory and to change the name of the file in 
'main()' if your text file is named differently."""

import random
import os
from datetime import datetime

def pass_generator():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    sybmols = "!@#$%?"
    n = lower + upper + numbers + sybmols
    length = 16
    global password
    password = "".join(random.sample(n, length))
    return password

def date():
    return datetime.today().strftime('%Y-%m-%d')

def add_to_file(filename):
    file = open(filename, "a")
    file.write(f"{input("What site  ")}: {password} | {date()}\n")
    file.close()

def main():
    print(f"Your new password is {pass_generator()}")
    add_to_file("saved-passwords.txt")

main()
