"""
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
2044. Count Number of Maximum Bitwise-OR Subsets
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
Example 1:
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
Constraints:
1 <= nums.length <= 16
1 <= nums[i] <= 105
Hint 1
Can we enumerate all possible subsets?
Hint 2
The maximum bitwise-OR is the bitwise-OR of the whole array.
"""
# Time - O(2^n or 2^17 or 2^n or n*2^n)
# Space - O(n or n+max_or or n or 1)

from collections import defaultdict
from copy import deepcopy
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # max_or = 0
        # for n in nums:
        #     max_or |= n
        # res = 0
        # def dfs(i, cur_or):
        #     nonlocal res, max_or
        #     if i ==  len(nums):
        #         res += 1 if cur_or == max_or else 0
        #         return 
        #     # skip i 
        #     dfs(i + 1, cur_or)
        #     # include i
        #     dfs(i + 1, cur_or | nums[i])
        # dfs(0, 0)
        # return res

        # Memoization
        # max_or = 0
        # for n in nums:
        #     max_or |= n
        # cache = [[-1] * (max_or + 1) for _ in range(len(nums))]
        # def dfs(i, cur_or):
        #     nonlocal max_or
        #     if i ==  len(nums):
        #         return 1 if cur_or == max_or else 0
        #     if cache[i][cur_or] != -1:
        #         return cache[i][cur_or]
        #     cache[i][cur_or] = dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])
        #     return cache[i][cur_or]
        # return dfs(0, 0)

        # dp = defaultdict(int) # key=cur_or val=cnt
        # dp[0] = 1
        # max_or = 0
        # for n in nums:
        #     new_dp = deepcopy(dp)
        #     for cur_or, cnt in dp.items():
        #         new_or = n | cur_or
        #         new_dp[new_or] += cnt 
        #     dp = new_dp
        #     max_or |= n
        # return dp[max_or]

        max_or = 0
        for n in nums:
            max_or |= n
        length = len(nums)
        res = 0
        for subset in range(1, 2**length):
            cur_or = 0
            for i in range(length):
                if 1 << i & subset:
                    cur_or |= nums[i]
            res += 1 if cur_or == max_or else 0
        return res

sol = Solution()
print(sol.countMaxOrSubsets(nums = [3,1]))
print(sol.countMaxOrSubsets(nums = [2,2,2]))
print(sol.countMaxOrSubsets(nums = [3,2,1,5]))
