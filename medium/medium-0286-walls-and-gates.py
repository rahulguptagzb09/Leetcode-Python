"""
https://leetcode.com/problems/walls-and-gates/
https://leetcode.ca/all/286.html
286. Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

# Time - O(n*m)
# Space - O(n*m)

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Graphs
        # Iterative Breadth First Search BFS
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def add_room(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.popleft()
                rooms[r][c] = dist
                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)
            dist += 1
        return rooms


sol = Solution()
print(
    sol.wallsAndGates(
        rooms=[
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
print(sol.wallsAndGates(rooms=[[-1]]))
