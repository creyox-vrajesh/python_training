# Write a Python program that computes a net bank balance based on a transaction log given as string input. D means Deposit and W means Withdrawal (e.g., "D 100 W 50 D 40")

# transaction_log = input("enter your transaction_log as string like \"D 100 W 50 D 40\":")
transaction_log = "D 100 W 150 D 40 "

transaction_log = transaction_log.split()

values = [int(i) for i in transaction_log if i.isdigit()]

keys = [i for i in transaction_log if i.isalpha()]
# print(keys,values)

dict1 = {}

for i in range(0,len(values)):
    if keys[i] in dict1:
        dict1[keys[i]] += values[i]
    else:
        dict1[keys[i]] = values[i]

total_deposit = dict1['D']

total_withdraw = dict1['W']

net_balance = total_deposit - total_withdraw

print(f"net bank balance is : {net_balance}") 
