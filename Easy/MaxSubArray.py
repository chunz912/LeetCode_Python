# -*- coding: utf-8 -*-
"""
solution 1
"""

def maxSubArray(self, nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)
    
"""
solution 2
思路：
    根据‘动态规划’和‘贪心算法’可以得出，
    解决此类问题的关键在于设置一个变量存放以当前元素为最长子数组的最后一个元素。
    用所能达到的最大和，以及之前所达到的最大和进行对比（
    这里是用到动态规划，需要理解与贪心算法的区别。动态规划可以保存之前的最大值）
    
思路：
    以下所写都是我在做题过程中想到的方法。
    首先判断正负，用第一个数和第二个数比较，如果第一个数>=第二个数,则两数相加，
    将得到的和存在一个变量中，与下一个数作比较。否则，从第二个数开始。用到递归调用。
"""
def maxSubArray(self, nums):
    if len(nums) == 0:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum
