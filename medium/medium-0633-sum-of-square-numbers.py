"""
https://leetcode.com/problems/sum-of-square-numbers/description/
633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: c = 3
Output: false
Constraints:
0 <= c <= 231 - 1
"""
# Time - O(c) or O(sqrt c)
# Space - O(1)

from math import sqrt

def judgeSquareSum(c: int) -> bool:
    # squareroot = set()
    # for i in range(int(sqrt(c)) + 1):
    #     squareroot.add(i * i)
    # a = 0
    # while a * a <= c:
    #     target = c - a * a
    #     if target in squareroot:
    #         return True
    #     a += 1 
    # return False
    
    left, right = 0, int(sqrt(c))
    while left <= right:
        total = left * left + right * right 
        if total > c:
            right -= 1
        elif total < c:
            left += 1
        else:
            return True
    return False

print(judgeSquareSum(c = 5))
print(judgeSquareSum(c = 3))
