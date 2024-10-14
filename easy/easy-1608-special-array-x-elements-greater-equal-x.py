"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
1608. Special Array With X Elements Greater Than or Equal X
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
"""

from typing import List

def specialArray(nums: List[int]) -> int:
    count = [0] * (len(nums) + 1 )
    for n in nums:
        index = n if n < len(nums) else len(nums)
        count[index] += 1
    total_right = 0
    for i in reversed(range(len(nums) + 1)):
        total_right += count[i]
        if i == total_right:
            return total_right
    return -1 

    # nums.sort()
    # i = 0
    # prev = -1
    # total_right = len(nums)
    # while i < len(nums):
    #     if nums[i] == total_right or (prev < total_right < nums[i]):
    #         return total_right
        
    #     while i + 1 < len(nums) and nums[i] == nums[i+1]:
    #         i += 1
        
    #     prev = nums[i]
    #     i += 1
    #     total_right = len(nums) - i
    
    return -1

print(specialArray(nums = [3,5]))
print(specialArray(nums = [0,0]))
print(specialArray(nums = [0,4,3,0,4]))