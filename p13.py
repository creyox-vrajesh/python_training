nums = list(map(int, input("enter numbers which have length between 3 and 13: ").split(',')))

if(len(nums)<3 or len(nums)>13):
    print("invalid input")
    exit()

for i in range(1,len(nums)-1):
    result =  True if (nums[i] - nums[i-1]) == 1 else False
    if not result:
        break

print("numbers in consecutive sequence" if result else "numbers are not in consecutive sequence") 