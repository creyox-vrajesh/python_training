# Write a Python program using recursion to count the frequency of each individual character in an input string.


def count_freq_char(str1,dict1):
    if not str1:
        return 1
    else:
        if str1[0] in dict1:
            dict1[str1[0]] += 1
        else:
            dict1[str1[0]] = 1

        count_freq_char(str1[1:],dict1)

        return dict1


dict1 = {}
dict1 = count_freq_char("hello my vrajesh",dict1)
print(dict1)
