# Write a Python program using recursion to count the frequency of each individual character in an input string.

def count_freq_char(str1):
    dict1 = {}
    
    if str1[-1]:
        dict1[str1[-1]] = str1[-1]
    else:
        if str1[-1] in dict1:
            dict1[str1[-1]] += 1
        else:            
            return  count_freq_char(str1[:-2])
    
    
    
print(count_freq_char("hello my name is mer vrajesh"))