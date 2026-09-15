# Write a Python program to take two lists—one with integer keys and one with string values—pair them together, and sort the pairs based on the values in the integer list

list1 = [3,2,1]
list2 = ["hi", "hello"]

# result = zip(list1,list2)
# for i in result:
#     print(i)

print(result)
dict1 = dict(zip(list1,list2))

dict1 = dict(sorted(dict1.items()))
print(dict1)