"""
https://leetcode.com/problems/number-of-enclaves/description/
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""
# Time - O(n*m)
# Space - O(m*n)

from typing import List


def numEnclaves(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    # Return num of land cells
    def dfs(r, c):
        if (r < 0 or c < 0 or r == ROWS or c == COLS or not grid[r][c] or (r, c) in visit):
            return 0
        visit.add((r, c))
        res = 1
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in direct:
            res += dfs(r + dr, c + dc)
        return res

    visit = set()
    land, borderLand = 0, 0
    for r in range(ROWS):
        for c in range(COLS):
            land += grid[r][c]
            if (grid[r][c] and (r, c) not in visit and (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                borderLand += dfs(r, c)
    
    return land - borderLand

print(numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
