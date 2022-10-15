import excelhelper

file = "styled.xlsx"

wb = load_workbook(filename=file)

sh = wb["Sheet"]

# shr = sh.rows
# shc = sh.columns

cells = ('B3', 'B8')

for cell in sh.iter_cols(0)):
	print(cell.value)

# for row in sh.rows:
#     for cell in row:
#         new_cell = sh.cell(row=cell.row, column=cell.col_idx,
#                                   value=cell.value)
#         if cell.has_style:
#             new_cell.font = copy(cell.font)
#             new_cell.border = copy(cell.border)
#             new_cell.fill = copy(cell.fill)
#             new_cell.number_format = copy(cell.number_format)
#             new_cell.protection = copy(cell.protection)
#             new_cell.alignment = copy(cell.alignment)-


# currStyle = NamedStyle(name="currStyle")


# wb.save("styled.xlsx")

data = [1, 2, 3, 4]

# def copyStyle(sheet, rows: tuple, cols: tuple):

# 	t_style = NamedStyle()

# 	for col in cols:
# 		for cell in col:
# 			if cell.has_style:
# 				t_style.font = copy(cell.font)
# 				t_style.border = copy(cell.border)
# 				t_style.fill = copy(cell.fill)
# 				t_style.number_format = copy(cell.number_format)
# 				t_style.protection = copy(cell.protection)
# 				t_style.alignment = copy(cell.alignment)



