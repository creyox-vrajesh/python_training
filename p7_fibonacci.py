# Write a Python program to generate the Fibonacci series up to $n$ terms using list comprehension.

n=7

list1 = [0,1]

fibo = [list1.append(list1[i]+list1[i+1]) for i in range(0,n-2)]
print(list1)