"""
https://leetcode.com/problems/pascals-triangle-ii/
119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:
Input: rowIndex = 0
Output: [1]
Example 3:
Input: rowIndex = 1
Output: [1,1]
Constraints:
0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List


def getRow(rowIndex: int) -> List[int]:
    res = [1]

    for i in range(rowIndex):
        next_row = [0] * (len(res) + 1)
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j + 1] += res[j]
        res = next_row

    return res

print(getRow(rowIndex = 3))
print(getRow(rowIndex = 0))
print(getRow(rowIndex = 1))
