# Write a Python program to find the closest pair of numbers (the pair with the smallest difference) from a comma-separated list of numbers provided by the user.


list1 = list(map(int, input("enter list of numbers : ").split(",")))

smallest_diff = abs(list1[0]-list1[1] if list1[0] > list1[1] else list1[1]-list1[0])
result = (list1[0], list1[1])

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if abs(list1[i] - list1[j]) < smallest_diff:
            smallest_diff = abs(list1[i] - list1[j])
            result = list(result)
            result = (list1[i],list1[j])
            result = tuple(result)

print(f"smallest pair with minimum difference : {result}")
