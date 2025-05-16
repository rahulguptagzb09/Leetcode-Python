"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
1277. Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
Hint 1
Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
Hint 2
Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.
"""
# Time - O(n^2)
# Space - O(n^2)

from collections import defaultdict
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        # cache = {}
        # def dfs(r, c):
        #     if r ==  ROWS or c ==  COLS or not matrix[r][c]:
        #         return 0
        #     if (r, c) in cache:
        #         return cache[(r, c)]
        #     cache[(r, c)] = 1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))
        #     return cache[(r, c)]
        # res = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         res += dfs(r, c)
        # return res

        dp = defaultdict(int)
        res = 0
        for r in range(ROWS):
            cur_dp = defaultdict(int)
            for c in range(COLS):
                if matrix[r][c]:
                    cur_dp[c] = 1 + min(dp[c], cur_dp[c - 1], dp[c - 1])
                    res += cur_dp[c]
            dp = cur_dp
        return res

sol = Solution()
print(sol.countSquares(matrix = [[0,1,1,1], [1,1,1,1], [0,1,1,1]]))
print(sol.countSquares(matrix = [[1,0,1], [1,1,0], [1,1,0]]))
