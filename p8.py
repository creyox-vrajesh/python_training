# Write a Python program to filter a list of numbers by keeping only the elements located at odd indices.

list1 = [1,2,3,4,5,6,7,8,9,10]

list1 = [list1[i] for i in range(len(list1)) if i%2!=0]

print(list1)