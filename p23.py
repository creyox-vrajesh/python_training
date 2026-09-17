# Write a Python program to print the calendar for a specific month and year (e.g., November 2014) using Python's built-in calendar module.

import calendar

input_month = input("Enter month name in string : ")
input_year = int(input("Enter year in digit : "))

dict1 = dict({(month.lower(),index) for index,month in enumerate(calendar.month_name)})

date = calendar.month(input_year, dict1[input_month])
print(date)