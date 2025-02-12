"""
https://leetcode.com/problems/out-of-boundary-paths/description/
576. Out of Boundary Paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
Hint 1
Is traversing every path feasible? There are many possible paths for a small matrix. Try to optimize it.
Hint 2
Can we use some space to store the number of paths and update them after every move?
Hint 3
One obvious thing: the ball will go out of the boundary only by crossing it. Also, there is only one possible way the ball can go out of the boundary from the boundary cell except for corner cells. From the corner cell, the ball can go out in two different ways. Can you use this thing to solve the problem?
"""
# Time - O(n*m)
# Space - O(m*n)

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    # ROWS, COLS = m, n
    # MOD = 10**9 +7
    # cache = {}
    # def dfs(r, c, moves):
    #     if (r < 0 or r == ROWS or c < 0 or c == COLS):
    #         return 1
    #     if moves == 0:
    #         return 0
    #     if (r, c, moves) in cache:
    #         return cache[(r, c, moves)]

    #     cache[(r, c, moves)] = ((dfs(r + 1, c, moves - 1) + dfs(r - 1, c, moves - 1)) % MOD + 
    #                             ((dfs(r, c + 1, moves - 1) + dfs(r, c - 1, moves - 1)) % MOD)) % MOD
    #     return cache[(r, c, moves)]
    # return dfs(startRow, startColumn, maxMove)

    ROWS, COLS = m, n
    MOD = 10**9 +7
    grid = [[0] * COLS for r in range(ROWS)]
    for m in range(1, maxMove + 1):
        tmp = [[0] * COLS for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if r + 1 == ROWS:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r+1][c]) % MOD
                if r - 1 < 0:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r-1][c]) % MOD
                if c + 1 == COLS:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r][c+1]) % MOD
                if c - 1 < 0:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r][c-1]) % MOD
        grid = tmp
    return grid[startRow][startColumn]


print(findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
