# TKINTER & GUI PROGRAMMING 
# Tkinter Form and Widgets 

# 1. Create a basic Tkinter window with a title. 
import tkinter as tk 
root = tk.Tk()
root.title("My First Window")
root.mainloop()

# 2. Create a form with Entry fields for Name and Age.
import tkinter as tk
tk.Label(root, text = "Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text = "Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# 3. Add a Submit button to print values from the form. 
def submit():
    print("Name: ", name_entry.get())
    print("Age: ", age_entry.get())
tk.Button(root, text = "Submit", command = submit).pack()

# 4. Create Radio buttons for Gender Selection. 
gender = tk.StringVAr()
tk.Radiobutton(root, text = "Male", variable = gender , value = "Male").pack()
tk.Radiobutton(root, text = "Female", variable = gender, value = "Female").pack()

# 5. Create Checkbuttons for Hobbies.
cricket = tk.StringVar()
reading  = tk.IntVar()
tk.Checkbutton(root, text = "Cricket", variable = cricket).pack()
tk.Checkbutton(root, text = "Reading", variable = reading).pack()

# ADVANCED WIDGETS AND LAYOUT 
# 6.Create a Listbox to select favorite fruits.
fruits = tk.Listbox(root, selectmode = tk.MULTIPLE)
for fruit in ['Apple', 'Banana', 'Orange']:
    fruits.insert(tk.END, fruit)
fruits.pack()

# 7. Create a Combobox for country selection. 
from tkinter import tk 
combo  = tk.Combobox(root, values = ["India", "USA", "UK"])
combo.pack()

# 8. Create a Text area for user feedback. 
feedback = tk.Text(root, height = 5, width = 30)
feedback.pack()

# 9. Display form a using a Label after Clicking a button.
def display_data():
    msg = f"Hello.{name_entry.get()}!"
    label.config(text = msg)

label = tk.Label(root, text =" DurexDuregesh" )
label.pack()
tk.Button(root, text = "Greet", command = display_data).pack()

# 10. Use grid layout to arrange widgets in rows and columns.
tk.Label(root, text = "Email").grid(row   = 0 , column = 0)
tk.Entry(root).grid(row = 0, column = 1)

# EXCEL DATA WRITITNG  WITH XLWINGS
# 11. Save form data to Excel using Xlwings.
import xlwings as xw 
def save_to_excel():
    wb = xw.Book('form_data.xlsx')
    sheet = wb.sheets[0]
    sheet.range("A1").value = "Nmae"
    sheet.range("A2").value = name_entry.get()

# 12. Append multiple entries to Excel rows dynamically.
def append_to_excel():
    wb = xw.Book('form_data.xlsx')
    sheet  = wb.sheets[0]
    last_row = sheet.range("A1").end('down').row + 1
    sheet.range(f"A{last_row}").value=name_entry.get()

# 13. Add gender and hobbies to Excel from the form.
def submit_all():
    wb = xw.Book('form_data.xlsx')
    sheet = wb.sheets[0]
    data = [
        name_entry.get(),
        age_entry.get(),
        gender.get(),
        "Cricket" if cricket.get()else
        "Reading" if reading.get()else
    ]
    sheet.range('A2').value = data

# 14. Write a selected listbox items to Excel.
def save_fruits():
    selected  = [fruits.get(i) for i in fruits.curselection()]
    wb = xw.Book(fruits.xlsx)
    wb.sheets[0].range('A1').value = selected

# 15. Save combobox(country) and feedback(Text) to Excel. 
def save_feedback():
    country  = combo.get()
    user_feedback = feedback.get("1.0", tk.END).strip()
    wb = xw.Book('feedback.xlsx')
    sheet = wb.sheets[0]
    sheet.range('A1').value = ["Country", "Feedback"]
    sheet.range('A2').value = [country, user_feedback]

# REPORT AUTOMATION WITH XLWINGS 
# Excel Report Tasks
# 16. Generate  a summary report with headers.
wb = xw.Book()
sheet = wb.sheets[0]
sheet.range("A1").value = ["Name", "Age", "Gender"]
sheet.range("A2").value = ["Durgesh", 34, "Male"]
wb.save('summary_report.xlsx')

# 17. Calculate total of values in Excel column.
sheet.range("B6").formula = "=SUM(B2:B5)"

# 18. Format Excel report (bold headers, cell color). 
sheet.range("A1: C1").api.Font.Bold = True 
sheet.range("A1: C1").color = (200, 200, 250)

# 19. Add chart based on form submission  counts.
chart = sheet.charts.add()
chart.chart_type = 'column_clustered'
chart.set_source_data(sheet.range("A1: B5"))

# 20. Export the final Excel file after Tkinter form submission.
def export_file():
    wb = xw.Book()
    sheet = wb.sheets[0]
    sheet.range("A1").value = ["Name", name_entry.get()]
    wb.save("final_export.xlsx")