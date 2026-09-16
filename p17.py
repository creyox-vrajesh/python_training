# Write a Python program that accepts a sentence from the user, splits it into words, sorts the words alphabetically, and prints them separated by commas.
list1 = list(input("enter sentence : ").split())
list1.sort()
print(list1)