"""
https://leetcode.com/problems/monotonic-array/description/
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
Example 1:
Input: nums = [1,2,2,3]
Output: true
Example 2:
Input: nums = [6,5,4,4]
Output: true
Example 3:
Input: nums = [1,3,2]
Output: false
Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""
# Time - O(n)
# Space - O(1)

from typing import List


def isMonotonic(nums: List[int]) -> bool:
    # if nums[-1] - nums[0] < 0:
    #     nums.reverse()
    # for i in range(len(nums) - 1):
    #     if not (nums[i] <= nums[1 + 1]):
    #         return False
    # return True

    increase, decrease = True, True
    for i in range(len(nums) - 1):
        if not (nums[i] <= nums[i + 1]):
            increase = False
        if not (nums[i] >= nums[i + 1]):
            decrease = False        

    return increase or decrease


print(isMonotonic(nums = [1,2,2,3]))
print(isMonotonic(nums = [6,5,4,4]))
print(isMonotonic(nums = [1,3,2]))
