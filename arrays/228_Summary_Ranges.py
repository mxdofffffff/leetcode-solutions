nums = [0,2,4,5,7]
def summary(nums):
    result=[]
    if not nums:
        return []
    start=nums[0]
    for i in range(len(nums)-1):
        if nums[i+1]!=nums[i]+1:
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            start = nums[i+1]

    if start == nums[-1]:
        result.append(str(nums[-1]))
    else:
        result.append(f"{start}->{nums[-1]}")
    return result
print(summary(nums))