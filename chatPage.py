from tkinter import *
import loginPage
from client import Client
import time
from threading import Thread

root = Tk()
c1=Client(loginPage.getvals())
def getvals():
    c1.send_message((Msgvalue.get()))

root.geometry("500x400")
Label(root, text="recever's name", font="comicsansms 15 bold", pady=15).pack()
Msgvalue = StringVar()
widget=Button(text="send", command=getvals).pack(side = BOTTOM,anchor='se')
MsgEntry = Entry(root, textvariable=Msgvalue, font="comicsansms 12 bold",bg='cyan').pack(side = BOTTOM,anchor='sw', fill="x", padx=36)

def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 1/10 of a second
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages

        for msg in new_messages:  # display new messages
            print(msg)

            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()


root.mainloop()
