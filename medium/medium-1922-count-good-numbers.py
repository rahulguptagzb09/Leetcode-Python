"""
https://leetcode.com/problems/count-good-numbers/
1922. Count Good Numbers
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
Example 1:
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:
Input: n = 4
Output: 400
Example 3:
Input: n = 50
Output: 564908303
Constraints:
1 <= n <= 1015
Hint 1
Is there a formula we can use to find the count of all the good numbers?
Hint 2
Exponentiation can be done very fast if we looked at the binary bits of n.
"""
# Time - O(logn)
# Space - O(logn)

import math


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def power(x, n):
            res = 1
            while n > 0:
                if n % 2:
                    res = (res * x) % mod
                n = n // 2
                x = (x * x) % mod
            return res

        even = math.ceil(n / 2)
        odd = n // 2
        return (power(5, even) * power(4, odd)) % mod

sol = Solution()
print(sol.countGoodNumbers(n = 1))
print(sol.countGoodNumbers(n = 4))
print(sol.countGoodNumbers(n = 50))
