# Write a Python program to create a new string where the last character of a given string is attached to both its front and back.

str1 = "hello"
str2 = ""
str2 = str1[:]

str2 = str2.replace(str2[0], str2[-1])

print(str1)
print(str2)

