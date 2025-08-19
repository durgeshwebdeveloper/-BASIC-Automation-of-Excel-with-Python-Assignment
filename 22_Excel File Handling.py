#  INTRODUCTION, INSTALLATION , READING / WRITING EXCEL DATA 

# 1. How to Install XLwings?
# pip install xlwings

# 2. Open an existing Excel file and print the value in A1.
import xlwings as xw 
wb = xw.Book('example.xlsx')
sheet = wb.sheets[0]
print(sheet.range('A1').value)

# 3. Write data to cell B2 in Excel.
sheet.range('B2').value = 'Hello, Excel'

# 4. Read a range of cells(A1: C3) into a list of lists. 
data = sheet.range('A1:C3').value
print(data)

# WORKING WITH TANGE AND CELLS 
# 5. Update multiple cells with values using Xlwings.
sheet.range('A1:C1').value = [10,20,30]

# 6. Perform a sum of two cells values and store the result.
val1 = sheet.range('A1').value
val2 = sheet.range('A2').value
sheet.range('A3').value = val1 + val2

# FORMATTING EXCEL USING PYTHON 
# 7. Change cell interior color to yellow and font to red.
cell = sheet.range('B2')
cell = sheet.range(255, 255, 0)    # Yellow Background
cell.api.Font.Color = 255   # Red font 

# 8. Apply bold, italic, and underline to cell A1. 
cell = sheet.range('A1')
cell.api.Font.Bold = True
cell.api.Font.Italic = True 
cell.api.Font.Underline = True 

# 9. Apply conditional formatting .highlight cells > 50.
sheet.range("A1:A10").api.FormatConditions.Add( Type = 1, Operator = 1, Formula1 = "=50")
sheet.range("A1: A10").api.FormatConditions(1).Interior.Color = 13551615

# CHARTS AND VISUALIZATION 
# 10. Create a bar chart from values in A1:A5.
chart  = sheet.charts.addd()
chart.chart_type = 'bar_clustered'
chart.set_source_data(sheet.range('A1: A5'))

# 11. Create a line chart using B1: B5.
chart = sheet.chart.add()
chart.chart_type = 'line'
chart.set_source_data(sheet.range('B1:B5'))

# 12. Create a pie chart using C1:C5.
chart = sheet.charts.add()
chart.chart_type = 'pie'
chart.set_source_data(sheet.range('C1:C5'))

# 13. Create a patterned chart (custom series styles).
chart = sheet.charts.add()
chart.chart_type = 'column_clustered'
chart.set_source_data(sheet.range('A1:B5'))
chart.api.SeriesCollection(1).Formate.Fill.Patterned(1)

# APPLYING EXCEL FUNCTIONS USING PYTHON (
# 14. Use VLOOKUP to find data from a table.
sheet.range('D1').formula =  '=VLOOKUP("Durgesh", A1:B10, 2, FALSE)'

# 15. Use Excel's UPPER text function in a cell.
sheet.range("B1").formula = '=UPPER(A1)'

# 16. Use TODAY() date function in excel.
sheet.range('C1').formula = '=TODAY()'

# 17. Use CONCAT to merge two cells.
sheet.range('D1').formula = '=CONCAT(A1, "", B1)'

# PIVOT TABLES AND CONSOLIDATION 
# 18. Create a pivot table from data in A1:C10.
import pandas as pd 
df = pd.DataFrame(sheet.range('A1').expand().value[1:], columns = sheet.range('A1').expand().value[0])
pivot_df = df.pivot_table(index = 'Name', values = 'Amount', aggfunc = 'sum')
xw.Book().sheets[0].range('A1').value = pivot_df

# 19. Combine data from the two sheets and create master sheet. 
wb = xw.Book('example.xlsx')
sheet1 = wb.sheets['Jan']
sheet2 = wb.sheets['Feb']
data1 = sheet1.range('A1').expand().value
data2 = sheet2.range('A1').expand().value
combined = data + data[1:]
master = wb.sheets.add('Master')
master.range('A1').value = combined 

# 20. Automate pivot creation and export to new workbook.
df = pd.DataFrame(sheet.range('A1').expand().value[1:], columns = sheet.range('A1').expand().value[0])
pivot = df.pivot_table(index = 'Category', values = 'Sales', aggfunc = 'sum')
new_book  = xw.Book()
new_book.sheets[0].range('A1').value = pivot
new_book.save('pivot_output.xlsx')