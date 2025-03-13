"""
https://leetcode.com/problems/score-after-flipping-matrix/description/
861. Score After Flipping Matrix
You are given an m x n binary matrix grid.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score after making any number of moves (including zero moves).
Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:
Input: grid = [[0]]
Output: 1
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
"""
# Time - O(n*m)
# Space - O(n*m or 1)

from typing import List


def matrixScore(grid: List[List[int]]) -> int:
    # ROWS, COLS = len(grid), len(grid[0])
    # # Flip rows
    # for r in range(ROWS):
    #     if grid[r][0] == 0:
    #         for c in range(COLS):
    #             grid[r][c] = 0 if grid[r][c] else 1
    # # Flip cols
    # for c in range(COLS):
    #     one_cnt = 0
    #     for r in range(ROWS):
    #         one_cnt += grid[r][c]
    #     if one_cnt < ROWS - one_cnt:
    #         for r in range(ROWS):
    #             grid[r][c] = 0 if grid[r][c] else 1
    # res = 0
    # for r in range(ROWS):
    #     for c in range(COLS):
    #         res += grid[r][c] << (COLS - c - 1)
    # return res

    ROWS, COLS  = len(grid), len(grid[0])
    res = ROWS * 2**(COLS - 1)
    for c in range(1, COLS):
        cnt = 0
        for r in range(ROWS):
            if grid[r][c] != grid[r][0]:
                cnt += 1
        cnt = max(cnt, ROWS - cnt)
        res += cnt * (2**(COLS - c - 1))
    return res

print(matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
print(matrixScore(grid = [[0]]))
