import tkinter as tk
from tkinter import *
from tkinter import ttk

import sys


class TableView(tk.Frame):

	def __init__(self, parent, xpos, ypos, width, height):
		'''Gunwo tabelka'''

		self.parentFrame = parent
		self.posX = xpos
		self.posY = ypos
		self.sW = width
		self.sH = height

		super(TableView, self).__init__(self.parentFrame, highlightbackground="grey",
			 highlightthickness=1, width=self.sW, height=self.sH)
		

		self._widgets = { }

		tk.Frame.place(self, relx=0.1)
		self.__update()

	def setPos(self, x, y):
		self.posX = x
		self.posY = Y

		# tk.Frame.place(self.parentFrame, )

	def addWidget(self, name : str, widget : tk.Frame, col, row):
		pass

	def removeWidget(self, name : str):
		pass

	def getWidget(self, name : str):
		pass

	def getWidget(self, index : int):
		pass

	def __update(self):
		self.pack()
		self.update()
