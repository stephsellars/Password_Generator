"""
This program is simply to create a unique 16-character password for
any site one may need it for. Once the script is executable, it can be
added to the desktop for easy access. 
Running the script will create said password and log it into the file given by the user, 
input what the site it is for, once inputted by the user. Just be sure to have this file 
and your text file in the same directory.
--- Created as a final project in CSCI-1302 in the spring of 2023 ---
"""

import random
from datetime import datetime

class OperationInputError(Exception):
    pass


class Main:
    "starts the program and user input decides what it will do"
    def __init__(self):
        self.operations = ['generate password', 'show existing passwords']

        print(self.operations)
        self.choice = input(f'Which of the above operations would you like to perfrom?\n')
        if not isinstance(self.choice, str) or self.choice not in self.operations:
            raise OperationInputError("\nexpected choice to be in given list above\nPlease try Again")
        
    def operate(self):
        "either runs code to generate new password or lists existing passwords"
        self.file = input("What is the name of your file?\n")
        if self.choice == "Generate password".lower():
            return Password(self.file).process()
        elif self.choice == "Show existing passwords".lower():
            file = open(self.file, 'r')
            for line in file:
                print(line.strip())

    
class Password(Main):
    "creates the majority of used variables and creates the new password"
    def __init__(self, file):
        self.filename = file
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.sybmols = "!@#$%?"
        self.all = self.lower + self.upper + self.numbers + self.sybmols
        self.length = 16
        self.newpass = "".join(random.sample(self.all, self.length))
        self.process()

    def process(self):
        self.pass_list = []
        self.pass_list.append(self.newpass)
        return AddToFile(self.pass_list).add_new_password(self.filename)
    

class Date(Main):
    "creates a date that will be logged with each password"
    def __init__(self):
        self.time = datetime.today().strftime('%Y-%m-%d')

    def date(self):
        return f"{self.time}"
            

class AddToFile(Password):
    "Takes the new password, asks what it is for, and logs the answer, newpass, and date stamp into the file"
    def __init__(self, L):
        self.List_of_passwords = L

    def add_new_password(self, file):
        site = input("What is this password for?\n")
        if not isinstance(site, str):
            raise TypeError("expected input to be a string")
        for p in enumerate(self.List_of_passwords):
            result = p[-1]
        self.filename = open(file, 'a')
        self.filename.write(f"{site}: {result} | {Date().date()}\n")
        self.filename.close()
        print(f"Your new password for {site} is {self.List_of_passwords[-1]}.\n")
        complete_operations()


def complete_operations():
    "Once complete, the function will prompt the user to either kill the program, or to run it again"
    finish = input("Are you all set? (Y/N)\n")
    if finish == 'yes'.lower() or finish == 'y'.lower():
        print("Thank you for using Password Generator!")
        quit()
    elif finish == 'no'.lower() or finish == 'n'.lower():
        Main().operate()
    else:
        print("That was a Yes or No question. Please try again.")
        complete_operations()
        
Main().operate()

