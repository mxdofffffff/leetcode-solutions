nums=[1,2,3]
def dublicate(nums):
    sl={}
    for i in range(len(nums)):
        if nums[i] in sl:
            return True
        sl[nums[i]]=i
    return False
print(dublicate(nums))

