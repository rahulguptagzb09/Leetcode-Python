"""
https://leetcode.com/problems/sqrtx/description/
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
Constraints:
0 <= x <= 231 - 1
"""
# Time - O(log n)

def mySqrt(x: int) -> int:
    l, r = 0, x
    res = 0
    while l <= r:
        m = l + ((r - l) // 2)
        if m**2 > x:
            r = m - 1
        elif m**2 < x:
            l = m + 1
            res = m
        else:
            return m

    return res

print(mySqrt(x = 4))
print(mySqrt(x = 8))
