# Write a Python program to filter and print the odd numbers from a list of integers from 1 to 15 using the filter() function alongside a lambda expression.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

result = list(filter(lambda x: x%2!=0 ,list1))
print(result)
