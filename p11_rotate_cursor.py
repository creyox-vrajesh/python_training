# # Write a Python program to display a rotating console cursor (spinner animation: |, /, -, \) on the command-line terminal that runs for a set time duration.

# time =  int(input("enter time in seconds"))
import time

# start = time.time()
# end = time.time() + 8
start = 1
end = 5
spinner = "|/-\\"

# print(spinner)
i=0
while start < end:
    print(f"{spinner[i]}",end="\r")
    if i == 3:
        i=0
        start+=1
        time.sleep(1)
    else:
        i+=1
        start+=1
        time.sleep(1)
