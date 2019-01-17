"""
solution
"""

def searchInsert(self, nums, target):
     return len([x for x in nums if x<target])
    
"""
my solution
"""

def searchInsert(nums, target):
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] < target and target < nums[i+1]:
            return i+1
