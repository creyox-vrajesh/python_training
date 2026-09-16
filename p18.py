# Write a Python program that continuously accepts numbers from the user until they type 'q'. Once stopped, it should calculate and print: the minimum, the maximum, the total sum, the average, the number with the longest digit length, and the pair of numbers with the smallest mathematical difference


user_input = input("enter 'q' to exit, else, enter a number : ")
# print(user_input)
min_num = 0 
max_num = 0 
sum_num = 0 
avg_num = 0 
longest_num = 0
list1 = [int(user_input)]

while user_input != 'q':
    user_input = input("enter 'q' to exit, else, enter a number :")
    if user_input.isdigit():
        list1.append(int(user_input))            
else:
    print(list1)
    min_num = min(list1)
    max_num = max(list1)
    sum_num = sum(list1)
    avg_num = sum_num/len(list1)
    longest_num = max_num
    print(longest_num,"long")
    diff = list1[0]-list1[1] if list1[0]>list1[1] else list1[1]-list1[0] 
    pair=(list1[0],list1[1])
    
    for i in range(0,len(list1)):
        for j in range(i+1, len(list1)):
            if abs(list1[i]-list1[j]) < diff:
                diff = abs(list1[i]-list1[j])
                pair = list(pair) 
                pair = (list1[i], list1[j])
                pair = tuple(pair)
# print(pair)
            
print(list1)
print(f"the minimum number is : {min_num}")
print(f"the maximum number is : {max_num}")
print(f"total sum is : {sum_num}")
print(f"the average of list is : {avg_num}")
print(f"the number with the longest digit length : {longest_num}")
print(f"the pair of numbers with the smallest mathematical difference : {pair}")

