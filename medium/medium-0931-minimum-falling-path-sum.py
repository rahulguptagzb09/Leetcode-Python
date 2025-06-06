"""
https://leetcode.com/problems/minimum-falling-path-sum/description/
931. Minimum Falling Path Sum
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""
# Time - O(n^2)
# Space   O(n^2 or 1)

from typing import List


def minFallingPathSum(matrix: List[List[int]]) -> int:
    # N = len(matrix)
    # cache = {}
    # def dfs(r, c):
    #     if r == N:
    #         return 0
    #     if c < 0 or c == N:
    #         return float("inf")
    #     if (r, c) in cache:
    #         return cache[(r, c)]
    #     res = matrix[r][c] + min(dfs(r + 1, c - 1), dfs(r + 1, c), dfs(r + 1, c + 1))
    #     cache[(r, c)] = res
    #     return res
    # res = float("inf")
    # for c in range(N):
    #     res = min(res, dfs(0, c))
    # return res

    N = len(matrix)
    for r in range(1, N):
        for c in range(N):
            mid = matrix[r - 1][c]
            left = matrix[r - 1][c - 1] if c > 0 else float("inf")
            right = matrix[r - 1][c + 1] if c < N - 1 else float("inf")
            matrix[r][c] = matrix[r][c] + min(mid, left, right)
    return min(matrix[-1])

print(minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
print(minFallingPathSum(matrix = [[-19,57],[-40,-5]]))
