from Tkinter import *

def show_entry_fields():
   print("Start Date: %s\nEnd Date: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Start Date:").grid(row=0, column=0)
Label(master, text="End Date:").grid(row=1, column=0)

e1 = Entry(master, text="test")
e2 = Entry(master)

e1.grid(row=0, column=1, padx=4, pady=4)
e2.grid(row=1, column=1, padx=4)

Button(master, text='Quit', command=master.quit, height=1, width=15).grid(row=3, column=1, sticky=E, pady=4, padx=4)
Button(master, text='Show', command=show_entry_fields, height=1, width=15).grid(row=3, column=0, sticky=W, pady=4, padx=4)

mainloop( )
