"""
https://leetcode.com/problems/spiral-matrix-iv/description/
2326. Spiral Matrix IV
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.
Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
Constraints:
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
Hint 1
First, generate an m x n matrix filled with -1s.
Hint 2
Navigate within the matrix at (i, j) with the help of a direction vector ⟨di, dj⟩. At (i, j), you need to decide if you can keep going in the current direction.
Hint 3
If you cannot keep going, rotate the direction vector clockwise by 90 degrees.
"""
# Time - O(n*m)
# Space - O(n*m)

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # left, right = 0, n
        # top, bottom  = 0, m
        # res = [[-1] * n for _ in range(m)]
        # while head:
        #     # left to right
        #     for i in range(left, right):
        #         if not head:
        #             return res
        #         res[top][i] = head.val
        #         head = head.next
        #     top += 1
        #     # top to bottom
        #     for i in range(top, bottom):
        #         if not head:
        #             return res
        #         res[i][right-1] = head.val
        #         head = head.next
        #     right -= 1
        #     # right to left
        #     for i in range(right - 1 , left - 1, -1):
        #         if not head:
        #             return res
        #         res[bottom-1][i] = head.val
        #         head = head.next
        #     bottom -= 1
        #     # bottom to top
        #     for i in range(bottom - 1 , top - 1, -1):
        #         if not head:
        #             return res
        #         res[i][left] = head.val
        #         head = head.next
        #     left -= 1
        # return res

        left, right = 0, n
        top, bottom  = 0, m
        grid = [[-1] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1, [-1, 0]]]
        r, c, d = 0, 0, 0 # current row, col and direction
        while head:
            dr, dc = directions[d]
            while head and left <= c < right and top <= r < bottom and grid[r][c] == -1:
                grid[r][c] = head.val
                head = head.next
                r, c = r + dr, c + dc
            r, c = r - dr, c - dc
            d = (d + 1) % 4
            dr, dc = directions[d]
            r, c = r + dr, c + dc
        return grid
