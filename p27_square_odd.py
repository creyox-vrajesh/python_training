#  Write a Python program that takes a comma-separated list of numbers as input from the user and uses list comprehension to print the square of each odd number in the list.


list1 = list(map(int, input("enter comma seperated numbers :").split(',')))

print(list1)

newlist = list(map(lambda item:  item**2,filter(lambda item:  item%2!=0,list1)))

print(newlist)