import pandas as pd
from datetime import datetime, timedelta
today = datetime.today().date()
df = pd.read_excel('employee.xlsx')
previous_dates = [(today - timedelta(days=i)).strftime('%d %B %Y') for i in range(1, 6)]
# print(previous_dates)
# print(df.columns.tolist())

today_date = today.strftime('%d %B %Y')

# 1) Findout how many employees marked WFH, WFO for today.

for i in df.columns.tolist():
    if i == today_date:
        print(f"Total employees marked WFH, WFO for today : ")
        print(df[[str(f'{i}')]].value_counts())
        
# 2) Findout how many employees marked WFH, WFO for the previous 5 days from the current date.

print("Last 5 days WFO and WFH : ")
for i in df.columns.tolist():
    if i in previous_dates:
        print(df[[str(f'{i}')]].value_counts())

# 3)Findout employee id who has not filled the attendance in all today and previous 5 days..
missing_attendance_employees = []
for index, row in df.iterrows():
    if row[previous_dates + [today_date]].isna().all():
        missing_attendance_employees.append(row['Emp ID'])

print("Employees with Missing Attendance:", missing_attendance_employees)
