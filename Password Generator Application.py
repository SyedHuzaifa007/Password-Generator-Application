# Importing Modules

from tkinter import *
import random

# Creating Window

# root = Tk()
# root.geometry('300x300')
# root.title('Password Generator Application')
# Label(root,text='Welcome to Password Generator Application', font='arial 10 bold').pack()
# Label(root,text='=========================================', font='arial 10 bold').pack()
# Label(root,text='You can create random secure passwords here', font='arial 9 bold').pack()
# Label(root,text='---------------------------------------------', font='arial 9 bold').pack()
# Label(root,text='Click the below button to generate a random\npassword of 8 digits', font='arial 8 bold').pack()

# Making Function
def generate_pswd():
# Making Characters
    FirstUpperCaseLetter = str(chr(random.randint(65,90)))
    SecondUpperCaseLetter = str(chr(random.randint(65,90)))
    FirstLowerCaseLetter = str(chr(random.randint(97,122))) 
    SecondLowerCaseLetter = str(chr(random.randint(97,122)))
    FirstSymbol = str(chr(random.randint(32,64)))
    SecondSymbol = str(chr(random.randint(32,64)))
    FirstNumber = str(random.randint(0,9))
    SecondNmber = str(random.randint(0,9))
# Joining Characters

    password = str(FirstUpperCaseLetter + FirstSymbol + FirstNumber + SecondUpperCaseLetter + SecondSymbol + SecondNmber + FirstLowerCaseLetter + SecondLowerCaseLetter)

# Shuffling the password for security

    def shuffle(string):
        list1 = list(password)
        shuffeld = random.shuffle(list1)
        password = str(shuffeld)

# Final Password

    print(password)

generate_pswd()

# root.mainloop()