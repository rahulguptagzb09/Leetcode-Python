"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
201. Bitwise AND of Numbers Range
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: left = 5, right = 7
Output: 4
Example 2:
Input: left = 0, right = 0
Output: 0
Example 3:
Input: left = 1, right = 2147483647
Output: 0
Constraints:
0 <= left <= right <= 231 - 1
"""
# Time - O(logn)
# Space - O(1)


def rangeBitwiseAnd(left: int, right: int) -> int:
    # res = 0
    # for i in range(32):
    #     bit = (left >> i) & 1
    #     if not bit:
    #         continue
    #     remain = left % (1 << (i + 1))
    #     diff = (1 << (i + 1)) - remain
    #     if right - left < diff:
    #         res = res | (1 << i)
    # return res

    i = 0
    while left != right:
        left = left >> 1
        right = right >> 1
        i += 1
    return left << i

print(rangeBitwiseAnd(left = 5, right = 7))
print(rangeBitwiseAnd(left = 0, right = 0))
print(rangeBitwiseAnd(left = 1, right = 2147483647))
