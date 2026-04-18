"""
https://leetcode.com/problems/search-a-2d-matrix/
74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# Time - O(logn+logm)
# Space - O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break
        if not top <= bottom:
            return False
        row = top + (bottom - top) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


sol = Solution()
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
)
