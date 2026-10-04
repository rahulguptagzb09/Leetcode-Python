"""
https://leetcode.com/problems/target-sum/
494. Target Sum
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:
Input: nums = [1], target = 1
Output: 1
Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

# Time - O(n*m)
# Space - O(n*m or n*m or n)

from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2-D Dynamic Programming
        # Brute Force Bottom Up Recursive Memoization Caching
        # cache = {}  # (index, cur_sum) -> num of ways

        # def backtrack(i, cur_sum):
        #     if (i, cur_sum) in cache:
        #         return cache[(i, cur_sum)]
        #     if i == len(nums):
        #         return 1 if cur_sum == target else 0
        #     cache[(i, cur_sum)] = backtrack(i + 1, cur_sum + nums[i]) + backtrack(
        #         i + 1, cur_sum - nums[i]
        #     )
        #     return cache[(i, cur_sum)]

        # return backtrack(0, 0)

        # Top Down Dynamic Programming
        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[0][0] = 1
        # # (0 elements, 0 sum) -> 1 way, 1 way to sum zero with first 0 elements
        # for i in range(len(nums)):
        #     for cur_sum, cnt in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += cnt
        #         dp[i + 1][cur_sum - nums[i]] += cnt
        # return dp[len(nums)][target]

        dp = defaultdict(int)
        dp[0] = 1  # (0 sum) -> 1 way, 1 way to sum to zero with first 0 elements
        for n in nums:
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + n] += count
                next_dp[cur_sum - n] += count
            dp = next_dp
        return dp[target]


sol = Solution()
print(sol.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print(sol.findTargetSumWays(nums=[1], target=1))
