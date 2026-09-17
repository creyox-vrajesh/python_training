# Write a Python program that accepts an integer (e.g., $N$) and computes the value formula of $N + NN + NNN + NNNN$. (For example, if the input is 9, the output is calculated as 9 + 99 + 999 + 9999).

user_input = int(input("enter a number : "))
result,temp = 0,0
if type(user_input) is int:
    for i in range(0,4):
        temp = temp * 10 + user_input
        result += temp

    print(result)