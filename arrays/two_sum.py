nums = [1,7,10,8]
target = 9

def solution(nums,target):
    sl={}
    for i,num in enumerate(nums):
        result = target - num
        if result in sl:
            return sl[result],i
        sl[num]=i
print(solution(nums,target))