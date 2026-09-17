# Write a Python program that computes a net bank balance based on a transaction log given as string input. D means Deposit and W means Withdrawal (e.g., "D 100 W 50 D 40")

# Write a Python function to calculate the net bank balance from an input string representing a transaction log string (same logic format as Program 10, but structured within a returning function)

# transaction_log = input("enter your transaction_log as string like \"D 100 W 50 D 40\":")

def calculate_net_balance(list1):
    dict1 = {}

    if len(list1) % 2 == 0:
        for i in range(0, len(list1), 2):
            if list1[i] in dict1:
                dict1[list1[i]] += int(list1[i+1])
            else:
                dict1[list1[i]] = int(list1[i+1])

        return dict1
    else:
        return 0

user_input = input("enter your transaction_log as string like 'D 100 W 50 D 40: ").split()

# result = {}
result = calculate_net_balance(user_input)

total_deposit = result["D"]
total_withdraw = result['W']

net_bank_balance = total_deposit - total_withdraw

print(f"total bank balance is : {net_bank_balance}")