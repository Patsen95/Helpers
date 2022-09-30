import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import width


""" TODO
	- option to add other widgets to status bar and correctly handle variable access to them
	- Tk.Style support to StatusBar class
	- Tk.StringVar support

	Bugs:
	- Check for key-duplicates
"""

class StatusBar(tk.Frame):
	"""StatusBar widget. Creates container area at the bottom inside the window"""
	_container = None

	def __init__(self, master):
		"""Construct the StatusBar object in a MASTER form.
		
		Args:
			master - parent form
		"""
		super(StatusBar, self).__init__(master, highlightbackground="grey", highlightthickness=1)
		self.pack(side=BOTTOM, fill=X)

		self._container = {}

	def addLabel(self, labelName : str, value, offset: int = 0):
		"""Add label with name, any-type value and optional X-offset.
			
		Args:
			labelName: str - label name
			value: any - value to display. Internally converter to text (str)
			offset: int - optional, determines left-side position offset, default 0
		
		Returns:
			Nothing
		"""
		label = tk.Label(self, text=str(value))
		label.pack(anchor="w", side=LEFT, padx=(offset, 0))
		self._container.update({labelName: label})
		self._update()

	def addSeparator(self, name: str, lpad: int, rpad: int = 0):
		"""Add vertical line to distinguish labels.

		Args:
			name: str - item's name
			lpad: int - left padding
			rpad: int - optional, right padding, deafult 0

		Returns:
			Nothing
		"""	
		label = tk.Label(self, text='|')
		label.pack(anchor="w", side=LEFT, padx=(lpad, rpad))
		self._container.update({name: label})
		self._update()

	def setValue(self, labelName: str, value):
		"""Set label's text. Can accept variables.

		Args:
			labelName: str - label's name
			value: any - value to display

		Returns:
			Nothing
		"""
		if not (self._container[labelName] == None):
			pass
		self._container[labelName].config(text=str(value))
		self._update()

	def labelOffset(self, labelName: str, offset: int):
		"""Set label's X-position.

		Args:
			labelName: str - label's name
			offset: int - X offset, relative to widget on the left side. 

		Returns:
			Nothing
		"""
		if not (self._container[labelName] == None):
			pass
		self._container[labelName].pack(padx=(offset, 0))
		self._update()

	def getLabel(self, labelName: str) -> tk.Label:
		"""Get Tk.Label object from StatusBar's container.

		Args:
			labelName: str - label's name

		Returns:
			tk.Label object stored in StatusBar's internal container
		"""
		if not (self._container[labelName] == None):
			pass
		return self._container[labelName]

	def deleteObject(self, name: str):
		"""Remove object from StatusBar.

		Args:
			name: str - object's name

		Returns:
			Nothing
		"""
		del self._container[name]
		self._update()

	def _update(self):
		"""Internal method."""
		self.pack()
