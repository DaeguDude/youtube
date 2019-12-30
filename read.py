import xlrd

xlsx_file = ("/Users/sanghakkim/Desktop/Youtube/read_excel/football_players_data.xlsx")

wb = xlrd.open_workbook(xlsx_file)
sheet = wb.sheet_by_index(0)


# sheet.cell_value(row, col)
print(sheet.cell_value(0, 5))

num_rows = sheet.nrows

ages = []
for i in range(1, num_rows):
    age = sheet.cell_value(i, 5)
    ages.append(age)

average_height_players = sum(ages) / len(ages)
print(average_height_players)
print(round(average_height_players, 2))

