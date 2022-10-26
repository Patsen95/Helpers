# coding=utf-8

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# from statusbar import *
# from tableview import *
from entrytable import *


class Application:

	def __init__(self):

		self.tk = Tk()
		self.tk.title("UI widgets Test")
		self.tk.geometry("320x240")
		self.window = ttk.Frame(self.tk)
		# self.window.grid()

		# sbar = StatusBar(self.tk)
		# sbar.addLabel("t1", "Test Label #1")
		# sbar.addLabel("t2", "Test Label #2", 10)
		# sbar.addSeparator("sep", 20)
		# sbar.addLabel("t3", "Test Label #3", 10)

		# tv = TableView(self.tk, 150, 50, 50, 50, 50, 50)
		# tv.setPos(850, 550)

		# self.window.grid()

		# names = ("This is col1", "col2", "col3", "trololoddddddddddddddd")
		names = ("This is col1", "oiawdoiawd")
		self.et = EntryTable(self.tk, 80, 100, 3, names)



		btn1 = Button(self.window, text="Delete row", command=self.click)
		btn1.grid(column=0, row=0)


		# self.et.deleteRow(2)


		self.window.pack()

	def click(self):
		self.et.deleteRow(0)
	
	def mainLoop(self):
		self.tk.mainloop()

	def close(self):
		self.tk.destroy


################################################

def main():
	appInstance = Application()	
	appInstance.mainLoop()


if __name__ == "__main__":
	main()
