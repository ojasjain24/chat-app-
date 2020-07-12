from tkinter import *
root = Tk()


def getvals():
    return uservalue.get()
root.geometry("200x150")
#Heading
Label(root, text="Welcome to chat", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
username = Label(root, text="Username").grid(row=1, column=2)
password = Label(root, text="password").grid(row=2, column=2)

# Tkinter variable for storing entries
uservalue = StringVar()
passvalue = StringVar()
remembervalue = IntVar()

#Entries for our form
userEntry = Entry(root, textvariable=uservalue).grid(row=1, column=3)
passEntry = Entry(root, textvariable=passvalue).grid(row=2, column=3)
rememberEntry = Checkbutton(text="Remember Me", variable = remembervalue).grid(row=6, column=3)


#Button & packing it and assigning it a command
widget=Button(text="submit", command=getvals).grid(row=7, column=3)
#widget.bind('<Button>',quit)



root.mainloop()