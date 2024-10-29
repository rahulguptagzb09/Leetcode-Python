"""
https://leetcode.com/problems/transpose-matrix/description/
867. Transpose Matrix
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
2 4 -1      2 -10 18
-10 5 11 -> 4 5 -7 
18 -7 6     -1 11 6
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
# Time - O(n*m)
# Space - O(n*m)

from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(matrix), len(matrix[0])
    res = [[0] * ROWS for _ in range(COLS)]
    for r in range(ROWS):
        for c in range(COLS):
            res[c][r] = matrix[r][c]
    return res


print(transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(transpose(matrix = [[1,2,3],[4,5,6]]))