nums = [1,2,3,4,6,7]
def summary(nums):
    result=[]
    start=nums[0]
    for i in range(len(nums)-1):
        if nums[i+1]!=nums[i]+1:
            if start == nums[i]:
                result.append(nums[-1])
            else:
                result.append(f"{start}->{nums[i]}")
            start = nums[i+1]
    if start == nums[-1]:
        result.append(nums[-1])
    else:
        result.append(f"{start}->{nums[-1]}")
    return result
print(summary(nums))