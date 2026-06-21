nums = [2,2,3]
def single(nums):
    sl={}
    for num in nums:
        if num in sl:
            sl[num]+=1
        else:
            sl[num]=1
    for k,value in sl.items():
        if value==1:
            return k
print(single(nums))