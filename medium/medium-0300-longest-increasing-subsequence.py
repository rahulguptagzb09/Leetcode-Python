"""
https://leetcode.com/problems/longest-increasing-subsequence/
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
# Time - O(n^2)
# Space - O(n)

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

sol = Solution()
print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS(nums = [0,1,0,3,2,3]))
print(sol.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
