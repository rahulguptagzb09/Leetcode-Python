"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
Hint 1
Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
Hint 2
The problem is now the cost of minimum spanning tree in graph with above edges.
"""

# Time - O(n^2 * logn)
# Space - O(n^2)

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}  # i -> list of (cost, node)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        # Prims
        res = 0
        visit = set()
        min_heap = [(0, 0)]  # (cost, point)
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_heap, (nei_cost, nei))
        return res


sol = Solution()
print(sol.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(sol.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
