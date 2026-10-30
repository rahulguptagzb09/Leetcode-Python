"""
https://leetcode.com/problems/integer-break/
343. Integer Break
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.
Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Constraints:
2 <= n <= 58
Hint 1
There is a simple O(n) solution to this problem.
Hint 2
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.
"""

# Time - O(n^2)
# Space - O(n)


class Solution:
    def integerBreak(self, n: int) -> int:
        # cache = {1: 1}

        # def dfs(num):
        #     if num in cache:
        #         return cache[num]
        #     cache[num] = 0 if num == n else num
        #     for i in range(1, num):
        #         val = dfs(i) * dfs(num - i)
        #         cache[num] = max(cache[num], val)
        #     return cache[num]

        # return dfs(n)

        # Dynamic Programming
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        return dp[n]


sol = Solution()
print(sol.integerBreak(n=2))
print(sol.integerBreak(n=10))
