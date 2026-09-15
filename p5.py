# Write a Python program that accepts three dates from the user (in YYYY-MM-DD format) and checks whether the third date falls chronologically between the first two dates

date1 = "2025-11-05"
date2 = "2025-11-03"
date3 = "2025-11-04"

# date1 = input("Enter date1 in YYYY-MM-DD format :")
# date2 = input("Enter date2 in YYYY-MM-DD format :")
# date3 = input("Enter date3 in YYYY-MM-DD format :")


date1 =  date1.split('-')
date2 =  date2.split('-')
date3 =  date3.split('-')

date1 = [int(x) for x in date1]
date2 = [int(x) for x in date2]
date3 = [int(x) for x in date3]

if date1 > date3 > date2:
    print("date3 is between date1 and date2")
elif date1 < date3 < date2:
    print("date3 is between date1 and date2")
else:
    print("date3 is not  between date1 and date2")