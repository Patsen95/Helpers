import tkinter as tk
from tkinter import *
from tkinter import ttk

import sys


class TableView(tk.Frame):
	"""Wrapper widget which adds functionality to arrange other tk widgets
			in grid-like (table) view with additional options.
	"""
	_posX = None
	_posY = None
	_sx = None
	_sy = None
	_cols = None
	_rows = None
	_drawFrame = None
	_container = None

	def __init__(self, parent, xpos: int, ypos: int, sX: int, sY: int, cols: int, rows: int):
		"""Construct the TableView object in a PARENT form.
		
		Args:
			parent - parent form
			xpos: int - X position
			ypos: int - Y position
			sX: int - X size
			sY: int - Y size
			cols: int - max size in columns
			rows: int - max size in rows
		"""
		self._posX = xpos
		self._posY = ypos
		self._sx = sX
		self._sy = sY
		self._cols = cols
		self._rows = rows
		self._drawBorder = False
		self._container = {}

		super(TableView, self).__init__(parent, width=self._sx, height=self._sy, borderwidth=1, 
			relief=GROOVE)
	
		self.config(background="cyan")
		self._update()

	def border(self, show: bool, borderStyle=GROOVE):
		self._drawBorder = show
		if self._drawBorder == True:
			self.config(relief=borderStyle)
		else:
			self.config(relief=FLAT)

	def setPos(self, x: int, y: int):
		self._posX = x
		self._posY = y
		self._update()

	def addWidget(self, name: str, widget: tk.Widget, col: int, row: int):
		if not self._wdgtExists(str):
			pass
		pass

	def removeWidget(self, name: str):
		pass

	def getWidget(self, name: str) -> tk.Widget:
		pass

	def _wdgtExists(self, name: str) -> bool:
		"""Internal method."""
		return (name in self._container)

	def _update(self, force: bool=False):
		"""Internal method."""
		self.pack()
		self.place(x=self._posX, y=self._posY)
	 	# Tcl's internal event loop doesn't have to be force-updated every time
		if force == True:
			self.update()
