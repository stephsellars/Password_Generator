"""
This program is simply to create a unique 16-character password for
any site one may need it for. Once the script is executable, it can be
added to the desktop for easy access. 
Running the script will create said password and log it into the file given by the user, 
input what the site it is for, once inputted by the user. If this file does not exist, 
# then the file will be created in the same directory that this script is stored.
--- Created as a final project in CSCI-1302 in the spring of 2023 ---
"""

import random
from datetime import datetime
import string

class SelectOperationToPerform:
    "starts the program and user input decides what it will do"
    def __init__(self):
        self.operations = ['generate password','custom password', 'show existing passwords']
        
    def operate(self):
        "either runs code to generate new password or lists existing passwords"
        print(self.operations)
        self.choice = input(f'Which of the above operations would you like to perform?\n')
        try:
            if self.choice.lower() == "generate password":
                return PasswordFile().default_pass()
            elif self.choice.lower() == "custom password":
                return PasswordFile().custom_pass()
            elif self.choice.lower() == "show existing passwords":
                return PasswordFile().view_pass()
            else:
                print("Your input was not an option, please try again.\n")
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
        except Exception as e:
            print("An error occurred: ", e)
        self.operate()

    def complete_operations(self):
        "Once complete, the function will prompt the user to either kill the program, or to run it again"
        finish = input("Are you all set? (Y/N)\n")
        if finish.lower() == 'yes' or finish.lower() == 'y':
            print("Thank you for using Password Generator!")
            quit()
        elif finish.lower() == 'no' or finish.lower() == 'n':
            SelectOperationToPerform().operate()
        else:
            print("That was a Yes or No question. Please try again.")
            self.complete_operations()


class PasswordFile:
    def __init__(self):
        self.file = input("What is the name of your file?\n")

    def default_pass(self):
        return Password(self.file)
    def custom_pass(self):
        return PasswordContents(self.file)
    def view_pass(self):
        with open(self.file, 'r') as file:
            for line in file:
                print(line.strip())
            SelectOperationToPerform().complete_operations()


class PasswordContents:
    def __init__(self, file):
        num_of_lower = input("How many lowercase characters do you want?\n")
        num_of_upper = input("How many uppercase characters do you want?\n")
        num_of_digits = input("How many digit characters do you want?\n")
        num_of_special = input("How many special characters would you like?\n")
        return Password(file, int(num_of_lower), int(num_of_upper), int(num_of_digits), int(num_of_special))


class Password:         
    "creates the majority of used variables and creates the new password"
    def __init__(self, file=None, num_of_lower=10, num_of_upper=2, num_of_digits=2, num_of_special=2):
        self.file = file
        self.pwd_chars = random.sample(string.ascii_lowercase, num_of_lower) + \
                            random.sample(string.ascii_uppercase, num_of_upper) + \
                            random.sample(string.digits, num_of_digits) + \
                            random.sample("!@#$%*?.", num_of_special)
        random.shuffle(self.pwd_chars)
        self.newpass = "".join(self.pwd_chars)
        self.process()

    def process(self):
        return AddToFile(self.newpass).add_new_password(self.file)
    

class Date:
    "creates a date that will be logged with each password"
    def __init__(self):
        self.time = datetime.today().strftime('%Y-%m-%d')

    def date(self):
        return f"{self.time}"
            

class AddToFile:
    "Takes the new password, asks what it is for, and logs the answer, newpass, and date stamp into the file"
    def __init__(self, strs):
        self.password = strs

    def add_new_password(self, file):
        site = input("What is this password for?\n")
        if not isinstance(site, str):
            raise TypeError("expected input to be a string")
        self.filename = open(file, 'a')
        self.filename.write(f"{site}: {self.password} | {Date().date()}\n")
        self.filename.close()
        print(f"Your new password for {site} is {self.password}\n")
        SelectOperationToPerform().complete_operations()



        
SelectOperationToPerform().operate()


