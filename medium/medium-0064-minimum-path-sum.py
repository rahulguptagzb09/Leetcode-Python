"""
https://leetcode.com/problems/minimum-path-sum/
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

# Time - O(n*m)
# Space - O(n*m)

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]
        res[rows - 1][cols] = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]


sol = Solution()
print(sol.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(sol.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
