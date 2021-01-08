# Importing Modules

from tkinter import *
import random

# Creating Window

root = Tk()
root.geometry('300x300')
root.title('Password Generator Application')
Label(root,text='Welcome to Password Generator Application', font='arial 10 bold').pack()
Label(root,text='=========================================', font='arial 10 bold').pack()
Label(root,text='You can create random secure passwords here', font='arial 9 bold').pack()
Label(root,text='---------------------------------------------', font='arial 9 bold').pack()
Label(root,text='Click the below button to generate a random\npassword of 8 digits', font='arial 8 bold').pack()




root.mainloop()