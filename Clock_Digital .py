from tkinter import * 
root = Tk()

import datetime
x = datetime.datetime.now()
root.configure(bg="grey1")

Label(text="Saksham Bharat Digital Date Time" , borderwidth=3 , relief=SUNKEN  , bg ="Powder blue", font="Sans  13 bold ").pack(fill="x")

Label(root ,text=x,  bg='red' ,  padx="76" , pady="68" , fg="yellow" , font="Sans 18  bold  " , borderwidth=10 , relief=GROOVE ).place(relx = 0.5, rely = 0.5, anchor = 'center')


Label(text="Saksham Bharat ", borderwidth=10 , relief=GROOVE, font="comicsansms 20 italic").pack(side="bottom", fill="x")

Label(text="Presented By",font="sans 20 bold", borderwidth=10 , relief=GROOVE).pack( side ="bottom")



root.mainloop()