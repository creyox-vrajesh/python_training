# Write a Python program that accepts a comma-separated list of values. Check if each value is exactly a 4-digit binary string consisting only of 1s and 0s, and then print the values that are cleanly divisible by 5.

list1 = input("enter comma seperated values : ").split(',')

for x in list1:
    if len(x) == 4:
        if(int(x,2) % 5 == 0):
            print(int(x,2))
    else:
        break

