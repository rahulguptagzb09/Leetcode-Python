"""
https://leetcode.com/problems/maximum-matrix-sum/
1975. Maximum Matrix Sum
You are given an n x n integer matrix. You can do the following operation any number of times:
Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
Constraints:
n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
Hint 1
Try to use the operation so that each row has only one negative number.
Hint 2
If you have only one negative element you cannot convert it to positive.
"""
# Time - O(n^2)
# Space - O(1)

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg_cnt = 0
        mat_min = float("inf")
        for row in matrix:
            for n in row:
                res += abs(n)
                mat_min = min(mat_min, abs(n))
                if n < 0:
                    neg_cnt += 1
        if neg_cnt & 1: # % 2 to check odd
            res -= 2 * mat_min
        return res

sol = Solution()
print(sol.maxMatrixSum(matrix = [[1,-1],[-1,1]]))
print(sol.maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]))
