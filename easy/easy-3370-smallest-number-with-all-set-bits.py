"""
https://leetcode.com/problems/smallest-number-with-all-set-bits/
3370. Smallest Number With All Set Bits
Easy
You are given a positive number n.
Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
Example 1:
Input: n = 5
Output: 7
Explanation:
The binary representation of 7 is "111".
Example 2:
Input: n = 10
Output: 15
Explanation:
The binary representation of 15 is "1111".
Example 3:
Input: n = 3
Output: 3
Explanation:
The binary representation of 3 is "11".
Constraints:
1 <= n <= 1000
Hint 1
Find the strictly greater power of 2, and subtract 1 from it.
"""

# Time - O(log n)
# Space - O(1)


class Solution:
    def smallestNumber(self, n: int) -> int:
        # res = 1
        # while n > res:
        #     res = (res << 1) | 1
        # return res

        # binary search
        l, r = 1, 10
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            x = 2**m - 1
            if x >= n:
                r = m - 1
                res = x
            else:
                l = m + 1
        return res


sol = Solution()
print(sol.smallestNumber(n=5))
print(sol.smallestNumber(n=10))
print(sol.smallestNumber(n=3))
