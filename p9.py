# Write a Python program to solve the "Chickens and Rabbits" math puzzle: Given the total number of heads (e.g., 35) and total legs (e.g., 94), calculate how many chickens and rabbits there are


total_heads = 35
total_legs = 94

if total_legs % 2 != 0:
    print("Invalid Input.\n")
else: 
    chicken, rabbit = 35, 0

    chicken_legs = total_heads * 2

    difference = total_legs - chicken_legs 

    extra_legs = difference

    rabbit = extra_legs//2

    chicken -= rabbit

    print(f"difference : {difference}")

    print(total_heads, total_legs)

    print(f"chicken : {chicken} , rabbit: {rabbit}")