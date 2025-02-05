"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/
1800. Maximum Ascending Subarray Sum
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
Hint 1
It is fast enough to check all possible subarrays
Hint 2
The end of each ascending subarray will be the start of the next
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        res = cur
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur += nums[i]
            else:
                cur = nums[i]
            res = max(res, cur)
        return res

sol = Solution()
print(sol.maxAscendingSum(nums = [10,20,30,5,10,50]))
print(sol.maxAscendingSum(nums = [10,20,30,40,50]))
print(sol.maxAscendingSum(nums = [12,17,15,13,10,11,12]))
