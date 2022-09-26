# coding=utf-8

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from p95.statusbar import *
from p95.tableview import *


class Application:

	def __init__(self):

		self.tk = Tk()
		self.tk.title("UI widgets Test")
		self.tk.geometry("800x600")
		self.window = ttk.Frame(self.tk)

		sbar = StatusBar(self.tk)
		sbar.addLabel("first", "label1")
		sbar.addLabel("sec", "label2", 10)
		sbar.addLabel("third", "trzeci!")
		sbar.addLabel("czw", None)


		sbar.labelOffset("third", 50)
		
		sbar.labelOffset("czw", 100)
		kupa = 3.14159
		sbar.setValue("czw", kupa)



		# btn = Button(self.window, text="Click me", command=self.onClick)
		# btn.pack()

		# tv = TableView(self.tk, 20, 100, 50, 50)
		
		
		# tv.place(relx=0)

		self.window.pack()
	
	def appMainLoop(self):
		self.tk.mainloop()

	def closeApp(self):
		self.tk.destroy
		
# button1 = Button(frm, height=5, width=10, text="WYPIERDALAJ", command=root.destroy).grid(column=0, row=1)
# button2 = Button(frm, text="KLIK", command=Dupa).grid(column=1, row=1)


################################################
def main():
	appInstance = Application()	
	appInstance.appMainLoop()


if __name__ == "__main__":
	main()
