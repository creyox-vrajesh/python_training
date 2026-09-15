import time

wait_time = 1
attempts = 0
max_tries = 5

while attempts < max_tries:
    print(f"attempt : {attempts +1} , wait time : {wait_time} seconds")
    time.sleep(wait_time)
    attempts += 1 
    wait_time *= 2


