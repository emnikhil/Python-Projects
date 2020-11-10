import random
from tkinter import *
from tkinter import messagebox

text = "abcdefghijklmnopqrstvvwxyz0123456789"
window = Tk()
window.title('Captcha Application')
window.geometry("300x200")
captcha = StringVar()
user_input = StringVar()

def set_captcha():
    s = random.choices(text, k = 7)
    captcha.set(''.join(s))

def check():
    if captcha.get() == user_input.get():
        messagebox.showinfo("Success", "Correct")
    else:
        messagebox.showinfo("Error", "Incorrect")
    set_captcha()

Label(window, textvariable = captcha, font = "Arial 18 bold").pack()
Entry(window, textvariable = user_input, font = "Arial 18 bold").pack(ipady = 7)
Button(window, command = check, text = "Check", font = "Arial 18 bold").pack()

set_captcha()
window.mainloop()