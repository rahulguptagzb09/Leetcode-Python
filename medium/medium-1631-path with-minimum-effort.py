"""
https://leetcode.com/problems/path-with-minimum-effort/description/
1631. Path With Minimum Effort
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
Hint 1
Consider the grid as a graph, where adjacent cells have an edge with cost of the difference between the cells.
Hint 2
If you are given threshold k, check if it is possible to go from (0, 0) to (n-1, m-1) using only edges of ≤ k cost.
Hint 3
Binary search the k value.
"""
# Time - O(n*m * 2^lognm)
# Space - O(n*m)

import heapq
from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:
    ROWS, COLS = len(heights), len(heights[0])
    minHeap = [[0, 0, 0]] # [diff, r, c]
    visit = set()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while minHeap:
        diff, r, c = heapq.heappop(minHeap)
        if (r, c) in visit:
            continue
        visit.add((r, c))
        if (r, c) == (ROWS - 1, COLS - 1):
            return diff
        for dr, dc in directions:
            newR, newC = r + dr, c + dc
            if (newR < 0 or newC < 0 or newR == ROWS or newC == COLS) or (newR, newC) in visit:
                continue
            newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
            heapq.heappush(minHeap, [newDiff, newR, newC])

print(minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]))
print(minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
