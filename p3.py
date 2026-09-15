# Write a Python program to clean up a nested dictionary (representing countries, states, and cities) by removing any empty lists from the lowest-level values.

dict1 = {
    'India' : {
        'Gujarat' : ["Rajkot","Surat"],
        'Maharashtra' : [],
    },
    'USA' : {
        'California' : ["Los Angeles","San Francisco"],
        'Texas' : []
    }
}

dict2 = {}

for country,val in dict1.items():
    for state,city in dict1[country].items():
        if city:
            if country not in dict2:
                dict2[country] = {}
            dict2[country][state] = city

print(dict1)
print(dict2)
        


