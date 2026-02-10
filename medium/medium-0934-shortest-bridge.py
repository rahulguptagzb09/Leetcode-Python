"""
https://leetcode.com/problems/shortest-bridge/description/
934. Shortest Bridge
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
Constraints:
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
# Time - O(n)
# Space - O(n)

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def invalid(r, c):
            return r < 0 or c < 0 or r == n or c == n

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        cur_r, cur_c = r + dr, c + dc
                        if invalid(cur_r, cur_c) or (cur_r, cur_c) in visit:
                            continue
                        if grid[cur_r][cur_c]:
                            return res
                        q.append([cur_r, cur_c])
                        visit.add((cur_r, cur_c))
                res += 1

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()

sol = Solution()
print(sol.shortestBridge(grid = [[0,1],[1,0]]))
print(sol.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
print(sol.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
