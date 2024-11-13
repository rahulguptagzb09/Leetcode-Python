"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
"""
# Time - O(n*m)
# Space - O(n+m or 1)

from typing import List


def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    # ROWS, COLS = len(matrix), len(matrix[0])
    # res = []
    # row_min = set()
    # for r in range(ROWS):
    #     row_min.add(min(matrix[r]))
    # col_max = set()
    # for c in range(COLS):
    #     cur_max = matrix[0][c]
    #     for r in range(ROWS):
    #         cur_max = max(cur_max, matrix[r][c])
    #     col_max.add(cur_max)
    # for n in row_min:
    #     if n in col_max:
    #         res.append(n)
    # return res

    # ROWS, COLS = len(matrix), len(matrix[0])
    # res = []
    # row_min = set()
    # for r in range(ROWS):
    #     row_min.add(min(matrix[r]))
    # for c in range(COLS):
    #     cur_max = matrix[0][c]
    #     for r in range(ROWS):
    #         cur_max = max(cur_max, matrix[r][c])
    #     if cur_max in row_min:
    #         res.append(cur_max)
    # return res

    ROWS, COLS = len(matrix), len(matrix[0])
    max_of_row_mins = float("-inf")
    for r in range(ROWS):
        row_min =  min(matrix[r])
        max_of_row_mins = max(row_min, max_of_row_mins)

    for c in range(COLS):
        col_max = matrix[0][c]

        for r in range(ROWS):
            col_max = max(col_max, matrix[r][c])
        if col_max == max_of_row_mins:
            return [col_max]
    return []

print(luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
print(luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(luckyNumbers(matrix = [[7,8],[1,2]]))
