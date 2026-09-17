# Write a Python program that takes a sentence as input and iterates over it to count the total number of upper-case letters and lower-case letters.

user_input = input("enter sentence : ")

user_input = user_input

upper_letter_count = 0
lower_letter_count = 0

for i in range(0,len(user_input)):
    print(user_input[i])
    if user_input[i].isupper():
        upper_letter_count += 1
    if user_input[i].islower():
        lower_letter_count += 1

print(f'upper letters toal count is : {upper_letter_count}')
print(f'lower letters toal count is : {lower_letter_count}')
