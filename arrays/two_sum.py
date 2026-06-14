nums = [2,7,10,8]
target = 9

def solution(numbers,target):
    sl = {}
    for i,num in enumerate(numbers):
        res = target - num
        if res in sl:
            print(sl[res],i)
        sl[num] = i

solution(nums,target)