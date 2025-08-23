"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
# Time - O(logn)
# Space - O(1)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bin_search(left_bias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    i = m
                    if left_bias:
                        r = m - 1
                    else:
                        l = m + 1
            return i

        left = bin_search(True)
        right = bin_search(False)
        return [left, right]

sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(sol.searchRange(nums = [], target = 0))
