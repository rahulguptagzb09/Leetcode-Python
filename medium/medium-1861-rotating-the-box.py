"""
https://leetcode.com/problems/rotating-the-box/
1861. Rotating the Box
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.
Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
Hint 1
Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].
Hint 2
Start iterating from the bottom of the box and for each empty cell check if there is any stone above it with no obstacles between them.
"""
# Time - O(n*m)
# Space - O(1)

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # ROWS, COLS = len(box), len(box[0])
        # for r in range(ROWS):
        #     i = COLS - 1
        #     for c in reversed(range(COLS)):
        #         if box[r][c] == "#":
        #             box[r][c], box[r][i] = box[r][i], box[r][c]
        #             i -= 1
        #         elif box[r][c] == "*":
        #             i = c - 1
        # res = []
        # for c in range(COLS):
        #     col = [] # this is a row after rotation
        #     for r in reversed(range(ROWS)):
        #         col.append(box[r][c])
        #     res.append(col)
        # return res

        ROWS, COLS = len(box), len(box[0])
        res = [["."] * ROWS for _ in range(COLS)]
        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    res[i][ROWS - r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    res[c][ROWS - r - 1] = "*"
                    i = c - 1
        return res

sol = Solution()
print(sol.rotateTheBox(box = [["#",".","#"]]))
print(sol.rotateTheBox(box = [["#",".","*","."], ["#","#","*","."]]))
print(sol.rotateTheBox(box = [["#","#","*",".","*","."], ["#","#","#","*",".","."], ["#","#","#",".","#","."]]))
