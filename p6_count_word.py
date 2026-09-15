#Write a Python program that accepts a sentence as input and counts the frequency of each word within the sentence.

sentence = "hello my name is vraj and again hello vraj"

list1 = sentence.split()

# list1 = [x for x in list1 if x.isalpha()]

dict1 = {}

# for x in list1:
#     dict1[x] = list1.count(x)

for x in list1:
    if x in dict1:
        dict1[x] +=1
    else:
        dict1[x] = 1


print(dict(sorted(dict1.items())))