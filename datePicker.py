#!/usr/bin/env python 

from Tkinter import *

class Application:
    def __init__(self, master=None):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=frame.quit)
        self.hi_there.pack(side=LEFT)
		
#	def say_hi(self):
#		print "hi there, everyone!"

def main():

	root = Tk()

	app = Application(root)

	root.mainloop()
	root.destroy() # optional; see description below
	

if __name__ == "__main__":
    main()
	