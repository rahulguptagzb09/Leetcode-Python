"""
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
1072. Flip Columns For Maximum Number of Equal Rows
You are given an m x n binary matrix matrix.
You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
Return the maximum number of rows that have all values equal after some number of flips.
Example 1:
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
Hint 1
Flipping a subset of columns is like doing a bitwise XOR of some number K onto each row. We want rows X with X ^ K = all 0s or all 1s. This is the same as X = X^K ^K = (all 0s or all 1s) ^ K, so we want to count rows that have opposite bits set. For example, if K = 1, then we count rows X = (00000...001, or 1111....110).
"""
# Time - O(n*m)
# Space - O(n)

from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in matrix:
            row_key = tuple(row)
            if row[0]:
                row_key = tuple([0 if n else 1 for n in row])
            count[row_key] += 1
        return max(count.values())

sol = Solution()
print(sol.maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))
print(sol.maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]]))
print(sol.maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))
