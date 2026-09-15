# Write a Python program to sort a dictionary of dictionaries based on the value of a specific nested key (e.g., a 'sequence' number).

dict1 = {
    "9":{
        "name": "nine"
    },
    "8":{
        "name": "eight"
    },
    "4":{
        "name": "four"
    }
}
    
dict2= {}
for k,v in sorted(dict1.items()):
    dict2[k] = v

print(dict2)