"""
https://leetcode.com/problems/non-decreasing-array/
665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.
Constraints:
n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            # decrease left element
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True

sol = Solution()
print(sol.checkPossibility(nums = [4,2,3]))
print(sol.checkPossibility(nums = [4,2,1]))
