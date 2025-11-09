"""
https://leetcode.com/problems/grid-game/
2017. Grid Game
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.
The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
Example 1:
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.
Example 2:
Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.
Example 3:
Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
Constraints:
grid.length == 2
n == grid[r].length
1 <= n <= 5 * 104
1 <= grid[r][c] <= 105
Hint 1
There are n choices for when the first robot moves to the second row.
Hint 2
Can we use prefix sums to help solve this problem?
"""
# Time - O(n)
# Space - O(n)

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        pre_row1, pre_row2 = grid[0].copy(), grid[1].copy()
        for i in range(1, N):
            pre_row1[i] += pre_row1[i - 1]
            pre_row2[i] += pre_row2[i - 1]
        res = float("inf")
        for i in range(N):
            top = pre_row1[-1] - pre_row1[i]
            bottom = pre_row2[i - 1] if i > 0 else 0
            second_robot = max(top, bottom)
            res = min(res, second_robot)
        return res

sol = Solution()
print(sol.gridGame(grid = [[2,5,4],[1,5,1]]))
print(sol.gridGame(grid = [[3,3,1],[8,5,2]]))
print(sol.gridGame(grid = [[1,3,1,15],[1,3,3,1]]))
