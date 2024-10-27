"""
https://leetcode.com/problems/power-of-four/description/
342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true
Constraints:
-231 <= n <= 231 - 1
Follow up: Could you solve it without loops/recursion?
"""
# Time - O(1)
# Space - O(1)

from math import log


def isPowerOfFour(n: int) -> bool:
    # if n == 1:
    #     return True
    # if n <= 0 or n % 4:
    #     return False
    # return isPowerOfFour(n // 4)

    return n > 0 and log(n, 4) % 1 == 0

print(isPowerOfFour(n = 16))
print(isPowerOfFour(n = 5))
print(isPowerOfFour(n = 1))
