"""
https://leetcode.com/problems/spiral-matrix-ii/description/
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:
Input: n = 1
Output: [[1]]
Constraints:
1 <= n <= 20
"""
# Time - O(n^2)
# Space - O(n^2)

from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    mat = [[0] * n for _ in range(n)]
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    val = 1
    while left <= right:
        # fill every val in top row 
        for c in range(left, right + 1):
            mat[top][c] = val
            val += 1
        top += 1

        # fill every val in right col
        for r in range(top, bottom + 1):
            mat[r][right] = val 
            val += 1
        right -= 1

        # fill every val in bottom row (reverse order)
        for c in range(right, left - 1, -1):
            mat [bottom][c] = val
            val += 1
        bottom -= 1

        # fill every val in left col (reverse order)
        for r in range(bottom, top - 1 , -1):
            mat[r][left] = val
            val += 1
        left += 1
    return mat
    
print(generateMatrix(n = 3))
print(generateMatrix(n = 1))
