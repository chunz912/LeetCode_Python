"""
solution 1
"""

def removeElement(self, nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start
    
    
"""
solution 2
"""

class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
        
        
"""
my solution
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
        
"""
return length and modified nums
"""

def removeElement(nums, val):
    index = 0
    newLen = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    newLen = len(nums) - index
    for i in range(0, newLen):
        nums.pop()
    return index, nums
