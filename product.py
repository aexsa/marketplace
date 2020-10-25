import xlrd

# Give the location of the file
loc = ('C:\\Users\\aexsa.alfyano\\Documents\\matketplaceproduct\\products.xlsx')

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)
# looping data per row
prods = []
for i in range(sheet.nrows):
    if i != 0:
        prods0 = sheet.cell_value(i, 1)
        prods1 = sheet.cell_value(i, 2)
        prods2 = sheet.cell_value(i, 3)
        prods3 = sheet.cell_value(i, 4)
        prods4 = sheet.cell_value(i, 5)
        prods5 = sheet.cell_value(i, 6)
        prods6 = sheet.cell_value(i, 7)
        products = prods0 + ", " + prods1+ ", " + prods2+ ", " + prods3+ ", " + prods4+ ", " + prods5+ ", " + prods6
        products = products.split(", ")

        prods.append([products[0], products[1], products[2], products[3], products[4], products[5], products[6]])
        # print(prods)
        # print(sheet.cell_value(i, 1))
        # print(sheet.row_values(i, 1))
print(prods)
