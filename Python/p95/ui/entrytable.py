import tkinter as tk
from tkinter import *
from tkinter import ttk



class EntryTable(tk.Frame):

	_posX = None
	_posY = None
	_mcols = None
	_mrows = None
	_drawBorder = None
	_container = None
	_colNames = None

	def __init__(self, parent: tk.Frame, xpos: int, ypos: int, maxRows: int, colNames: tuple):

		self._posX = xpos
		self._posY = ypos
		self._mcols = len(colNames)
		self._mrows = maxRows
		self._drawBorder = True
		self._container = []
		self._colNames = colNames

		super(EntryTable, self).__init__(parent, width=self._mcols, height=self._mrows, borderwidth=1,
                                  relief=GROOVE)
		self._makeTable()
		self._update()

	def addRow(self):
		pass

	def deleteRow(self, row: int):
		start_idx = self._mcols + self._toIdx(row, 0)
		del self._container[start_idx: start_idx + self._mcols]
		self._mrows -= 1
		self._redrawTable()

	def clearCell(self, row: int, col: int):
		self._container[self._mcols + self._toIdx(row, col)].delete(0, END)

	def clearCellByIndex(self, index: int):
		self._container[self._mcols + index].delete(0, END)

	def setCell(self, row: int, col: int, value: float):
		entry = self._container[self._mcols + self._toIdx(row, col)]
		entry.delete(0, END)
		entry.insert(0, str(value))

	def setCellByIndex(self, index: int, value: float):
		entry = self._container[self._mcols + index]
		entry.delete(0, END)
		entry.insert(0, str(value))

	def getCell(self, row: int, col: int) -> float:
		return float(self._container[self._mcols + self._toIdx(row, col)].get())

	def getCellByIndex(self, index: int) -> float:
		return float(self._container[self._mcols + index].get())

	def getObject(self, row: int, col: int) -> tk.Entry:
		return self._container[self._toIdx(row, col)]

	def getObjectByIndex(self, index: int) -> tk.Entry:
		return self._container[index]

	def _makeTable(self):
		for r in range(self._mrows + 1):
			for c in range(self._mcols):
				idx = self._toIdx(r, c)
				if r == 0:
					label = tk.Label(self, text=str(self._colNames[c]))
					label.config(bd=1, relief=SUNKEN, justify=CENTER, padx=10)
					label.grid(row=r, column=c, sticky=E+W)
					self._container.insert(idx, label)
				else:
					entry = tk.Entry(self)
					entry.insert(0, str(idx - self._mcols))
					entry.config(exportselection=0, justify=CENTER, width=10)
					entry.grid(row=r, column=c, sticky=E+W)
					self._container.insert(idx, entry)

	def _redrawTable(self):
		for wdg in self.winfo_children():
			wdg.destroy()
			
		for r in range(self._mrows):
			for c in range(self._mcols):
				idx = self._toIdx(r, c)
				if r == 0:
					label = self._container[idx]
					label.grid(row=r, column=c, sticky=E+W)
				else: 
					entry = self._container[idx]
					entry.grid(row=r, column=c, sticky=E+W)
		self._update()


	def _toIdx(self, r: int, c: int):
		return (r * self._mcols) + c

	def _toRC(self, i: int):
		return (int(i / self._mcols), int(i % self._mcols))

	def _update(self, force: bool=False):
		"""Internal method."""
		self.pack()
		self.place(x=self._posX, y=self._posY)
	 	# Tcl's internal event loop doesn't have to be force-updated every time
		if force == True:
			self.update()

