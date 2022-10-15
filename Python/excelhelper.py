from openpyxl.styles import NamedStyle
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
from copy import copy



def getCellCoord(cellCoord: str) -> tuple(int, int):
	""" Converts Excel's cell literal address to row / column index.

	Args:
		cellCoord: str - cell's literal address

	Returns:
		Tuple with row and column indexes.
	"""
	coord = coordinate_from_string(cellCoord)
	col = column_index_from_string(coord[0])
	row = coord[1]
	return tuple(row, col)



