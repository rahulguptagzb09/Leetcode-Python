"""
https://leetcode.com/problems/arranging-coins/description/
441. Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
Constraints:
1 <= n <= 231 - 1
"""
# Time - O(logn)
# Space - O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res

sol = Solution()
print(sol.arrangeCoins(n = 5))
print(sol.arrangeCoins(n = 8))
