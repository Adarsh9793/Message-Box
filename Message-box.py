# step!: import tkinter
from tkinter import *
import tkinter.messagebox

# step2: gui interaction
window = Tk()


# step3: adding inputs
tkinter.messagebox.showerror("Error", "This is an error message")
question = tkinter.messagebox.askquestion("Question", "Do you want to proceed?")

if question == "True":
    print("User chose to proceed")
else:
    print("User chose not to proceed")

# step4: mainloop
mainloop()