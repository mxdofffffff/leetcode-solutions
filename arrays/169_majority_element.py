nums = [4,2,3]
def majority(nums):
    sl={}
    for num in nums:
        if num in sl:
            sl[num]+=1
        else:
            sl[num] = 1
    for k,value in sl.items():
        if value>len(nums)//2:
            return k
print(majority(nums)
