import tkinter as tk
from tkinter import *
from tkinter import ttk


	# TODO Handling Entry input event

class EntryTable(tk.Frame):

	_posX = None
	_posY = None
	_mcols = None
	_mrows = None
	_drawBorder = None
	_dataCache = None
	_colNames = None
	_currRows = None
	_currCols = None

	def __init__(self, parent: tk.Frame, xpos: int, ypos: int, maxRows: int, colNames: tuple):

		self._posX = xpos
		self._posY = ypos
		self._mcols = len(colNames)
		self._mrows = maxRows
		self._drawBorder = True
		self._dataCache = []
		self._colNames = list(colNames)
		self._currRows = []
		self._currCols = []

		super(EntryTable, self).__init__(parent, width=self._mcols, height=self._mrows, borderwidth=1,
                                  relief=GROOVE)

		self._dataCache.insert(0, 0)
		self._dataCache.insert(1, 1)
		self._dataCache.insert(2, 2)
		self._dataCache.insert(3, 3)
		self._dataCache.insert(4, 4)
		self._dataCache.insert(5, 5)

		for r in range(maxRows):
			self._currRows.insert(r, r)

		for c in range(self._mcols):
			self._currCols.insert(c, c)

		print(self._mcols, self._currCols, self._colNames)

		self._draw()


	def addRow(self):
		pass

	def addColumn(self):
		pass

	def deleteRow(self, row: int):
		if self._mrows > 0:
			if row in self._currRows: # TODO Check if selected row exists
				start_idx = self._toIdx(row, 0)
				del self._dataCache[start_idx : start_idx + self._mcols]
				del self._currRows[row : row + 1]
				self._mrows -= 1
				self._draw()

	def deleteColumn(self, col: int): # FIXME Not working?
		if self._mcols > 0:
			if col in self._currCols:
				start_idx = self._toIdx(0, col)
				del self._dataCache[start_idx : start_idx + self._mcols]
				del self._colNames[start_idx: start_idx + self._mcols]
				del self._currCols[col : col + 1]
				self._mcols -= 1
				self._draw()
				print(self._mcols, self._currCols, self._colNames)

	def clearCell(self, row: int, col: int):
		self._dataCache[self._mcols + self._toIdx(row, col)].delete(0, END)

	def clearCellByIndex(self, index: int):
		self._dataCache[self._mcols + index].delete(0, END)

	def setCell(self, row: int, col: int, value: float):
		entry = self._dataCache[self._mcols + self._toIdx(row, col)]
		entry.delete(0, END)
		entry.insert(0, str(value))

	def setCellByIndex(self, index: int, value: float):
		entry = self._dataCache[self._mcols + index]
		entry.delete(0, END)
		entry.insert(0, str(value))

	def getCell(self, row: int, col: int) -> float:
		return float(self._dataCache[self._mcols + self._toIdx(row, col)].get())

	def getCellByIndex(self, index: int) -> float:
		return float(self._dataCache[self._mcols + index].get())

	# def getObject(self, row: int, col: int) -> tk.Entry:
	# 	return self._dataCache[self._toIdx(row, col)]

	# def getObjectByIndex(self, index: int) -> tk.Entry:
	# 	return self._dataCache[index]

	def _draw(self):
		for wdg in self.winfo_children():
			wdg.destroy()
			
		for r in range(self._mrows + 1):
			for c in range(self._mcols):
				idx = self._toIdx(r, c)
				if r == 0:
					label = tk.Label(self, text=str(self._colNames[c]))
					label.config(bd=1, relief=SUNKEN, justify=CENTER, padx=10)
					label.grid(row=r, column=c, sticky=E+W)
				else: 
					entry = tk.Entry(self)
					if self._dataCache:
						dataIndex = idx - self._mcols
						if dataIndex <= len(self._dataCache) - 1:
							entry.insert(0, str(self._dataCache[dataIndex]))
					entry.config(exportselection=0, justify=CENTER, width=10)
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
