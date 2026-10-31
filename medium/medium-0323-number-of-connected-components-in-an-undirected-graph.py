"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
https://leetcode.ca/all/323.html
323. Number of Connected Components in an Undirected Graph
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.
Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
     0          3
     |          |
     1 --- 2    4
Output: 2
Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""

# Time - O(n*2)
# Space - O(n)

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Graphs
        # Union Find
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # path compression optimization
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


sol = Solution()
print(sol.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
print(sol.countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
