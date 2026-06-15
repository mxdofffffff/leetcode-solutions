nums=[9,9,9]
def number(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i]!=9:
            nums[i]+=1
            return nums
        nums[i]=0
    return [1]+nums
print(number(nums))