"""
https://leetcode.com/problems/number-of-closed-islands/description/
1254. Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.
Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
# Time - O(n*m)
# Space - O(n*m)

from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    def dfs(r, c):
        if (r < 0 or c < 0 or r == ROWS or c == COLS):
            return 0 # False
        if grid[r][c] == 1 or (r, c) in visit:
            return 1 # True
        visit.add((r, c))
        return min(dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1))

    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            if not grid[r][c] and (r, c) not in visit:
                res += dfs(r, c)
    return res

print(closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
