"""
https://leetcode.com/problems/maximal-square/description/
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:
Input: matrix = [["0"]]
Output: 0
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
# Time - O(n*m)
# Space - O(n*m)

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming bottom up
        # recursive top down
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # map each (r, c) -> max length of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diagonal = helper(r + 1, c + 1)
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diagonal)
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

sol = Solution()
print(sol.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(sol.maximalSquare(matrix = [["0","1"],["1","0"]]))
print(sol.maximalSquare(matrix = [["0"]]))
