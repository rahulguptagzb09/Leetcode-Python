"""
https://leetcode.com/problems/unique-paths-ii/description/
63. Unique Paths II
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
# Tim e- O(n*m)
# Space - O(n*m or n)

from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    # M, N = len(obstacleGrid), len(obstacleGrid[0])
    # dp = {(M - 1, N - 1): 1}
    # def dfs(r, c):
    #     if r == M or c == N or obstacleGrid[r][c]:
    #         return 0
    #     if (r, c) in dp:
    #         return dp[(r, c)]
    #     dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
    #     return dp[(r, c)]
    # return dfs(0, 0)
    
    M, N = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * N
    dp[N - 1] = 1
    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if obstacleGrid[r][c]:
                dp[c] = 0
            elif c + 1 < N: 
                dp[c] = dp[c] + dp[c + 1]
    return dp[0]

print(uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]]))
