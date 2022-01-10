# practice exercise done by yara
# countdown timer homework !
# let's do this ..
# 09.01.22

from tkinter import *
from requests import *

programWindow = Tk()

# create 3 variables for time
# hour
# minute
# second

hour = StringVar()
minute = StringVar()
second = StringVar()

# set the three variables to 0
# hour.set("00")
# minute
# second

hour.set("00")
minute.set("00")
second.set("00")

# Configure the window to take the following attributes
# title
programWindow.title("yaras countdown timer made for the whole globe")
# size
programWindow.geometry("500x600")
# background color
programWindow.config(bg="#D77FA1")
# font
titleLable = Label(text="yaras countdown timer made for the whole globe", font="times 12 bold", bg = "#BAFFB4")
titleLable.pack(pady=20)

hoursInput = Entry(textvariable=hour)
# pack the input box
hoursInput.pack()

minuteInput = Entry(textvariable=minute)
# pack the input box
minuteInput.pack()

secondInput = Entry(textvariable=second)
# pack the input box
secondInput.pack()


def submitTime():
    print("hello")
    # store time given by user in a var
    try:
        user_input = int(hour.get())+int(minute.get())+int(second.get())
    except:
        print("please use numbers only")


beginCountDown = Button(text="begin", command=submitTime)
# pack the button and set the text to "Begin Countdown"
beginCountDown.pack(padx = 20, side=RIGHT)

# create a button that will reset the timer by deleting whats inside the input fields
# and set the text to "Reset"



def resetButtonFunc():
    hour.set("00")
    minute.set("00")
    second.set("00")

resetButton = Button(text="reset", command=resetButtonFunc)
resetButton.pack(padx=20,side = LEFT)

closeButton =Button(text="close", command=programWindow.destroy)
closeButton.pack(pady=20, side = BOTTOM)

mainloop()
#end of code