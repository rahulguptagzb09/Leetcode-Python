"""
https://leetcode.com/problems/largest-divisible-subset/description/
8. Largest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""
# Time - O(n^2)
# Space - O(n^2)

from typing import List


def largestDivisibleSubset(nums: List[int]) -> List[int]:
    # Recursive 
    # nums.sort()
    # cache = {}
    # def dfs(i):
    #     if i == len(nums):
    #         return []
    #     if i in cache:
    #         return cache[i]
    #     res = [nums[i]]
    #     for j in range(i + 1, len(nums)):
    #         if nums[j] % nums[i] == 0:
    #             tmp = [nums[i]] + dfs(j)
    #             if len(tmp) > len(res):
    #                 res = tmp
    #     cache[i] = res
    #     return res
    # res  = []
    # for i in range(len(nums)):
    #     tmp = dfs(i)
    #     if len(tmp) > len(res):
    #         res = tmp
    # return res

    # Tabulation 
    nums.sort()
    dp = [[n] for n in nums] # dp[i] = longest start at i
    res = []
    for i in reversed(range(len(nums))):
        for j in range(i + 1, len(nums)):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dp[j]
                dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
        res = dp[i] if len(dp[i]) > len(res) else res
    return res

print(largestDivisibleSubset(nums = [1,2,3]))
print(largestDivisibleSubset(nums = [1,2,4,8]))
