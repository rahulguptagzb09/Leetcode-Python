"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
673. Number of Longest Increasing Subsequence
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.
Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
Constraints:
1 <= nums.length <= 2000
-106 <= nums[i] <= 106
The answer is guaranteed to fit inside a 32-bit integer.
"""
# Time - O(n^2)
# Space - O(n)

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} # index -> length of LIS, count
        len_lis, res = 0, 0 # length of LIS, count of LIS
        for i in range(len(nums) -1, -1, -1):
            max_len, max_cnt = 1, 1 # len, cnt of LIS start from i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]: # increasing order
                    length, count = dp[j] # len, cnt of LIS start from j
                    if length + 1 > max_len:
                        max_len, max_cnt = length + 1, count
                    elif length + 1 == max_len:
                        max_cnt += count
            if max_len > len_lis:
                len_lis, res = max_len, max_cnt
            elif max_len == len_lis:
                res += max_cnt
            dp[i] = [max_len, max_cnt]
        return res

sol = Solution()
print(sol.findNumberOfLIS(nums = [1,3,5,4,7]))
print(sol.findNumberOfLIS(nums = [2,2,2,2,2]))
