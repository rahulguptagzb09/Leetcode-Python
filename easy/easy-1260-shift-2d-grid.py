"""
https://leetcode.com/problems/shift-2d-grid/description/
1260. Shift 2D Grid
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
Hint 1
Simulate step by step. move grid[i][j] to grid[i][j+1]. handle last column of the grid.
Hint 2
Put the matrix row by row to a vector. take k % vector.length and move last k of the vector to the beginning. put the vector to the matrix back the same way.
"""
# Time - O(n*m)
# Space - O(n*m)

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        def post_to_val(r, c):
            return r * N + c
        def val_to_pos(v):
            return [v // N, v % N] # r, c

        res = [[0] * N for i in range(M)]
        for r in range(M):
            for c in range(N):
                new_val = (post_to_val(r, c) + k) % (M * N)
                new_r, new_c = val_to_pos(new_val)
                res[new_r][new_c] = grid[r][c]
        return res

sol = Solution()
print(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(sol.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))
