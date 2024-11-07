"""
https://leetcode.com/problems/power-of-two/description/
231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:
Input: n = 3
Output: false
Constraints:
-231 <= n <= 231 - 1
Follow up: Could you solve it without loops/recursion?
"""
# Time - O(logn or 1)
# Space - O(1)

def isPowerOfTwo(n: int) -> bool:
    # x = 1
    # while x < n:
    #     x *= 2
    # return x == n

    # return n > 0 and (n & (n - 1)) == 0
    
    # return n > 0 and (2**30 % n) == 0

    return n > 0 and ((1 << 30) % n) == 0

print(isPowerOfTwo(n = 1))
print(isPowerOfTwo(n = 16))
print(isPowerOfTwo(n = 3))
