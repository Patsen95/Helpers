import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import width


class StatusBar(tk.Frame):

	def __init__(self, parent):
		"""StatusBar UI widget class."""

		super(StatusBar, self).__init__(parent, highlightbackground="grey",
                                  highlightthickness=1)
		# self.grid(sticky="sw")
		self.pack(side=BOTTOM, fill=X)

		self._container = { }		

	def addLabel(self, labelName : str, value, xOffset : int = 0):
		_label = tk.Label(self, text=value)
		_label.pack(anchor="w", side=LEFT, padx=(xOffset, 0))	
		self._container.update({labelName: _label})
		self.__update()

	def setValue(self, labelName : str, value):
		if not (self._container[labelName] == None):
			pass
		self._container[labelName].config(text=value)
		self.__update()

	def labelOffset(self, labelName: str, offset : int):
		if not (self._container[labelName] == None):
			pass
		self._container[labelName].pack(padx=(offset, 0))
		self.__update()

	def getLabel(self, labelName : str):
		if not (self._container[labelName] == None):
			pass
		return self._container[labelName]

	def deleteLabel(self, name):
		del self._container[name]
		self.__update()

	def __update(self):
		self.pack()

