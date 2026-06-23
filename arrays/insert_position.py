nums=[1,3,3,4,5,6]
target = 5
def insert_position(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2  #index
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(insert_position(nums,target))