"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/
1129. Shortest Path with Alternating Colors
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
You are given two arrays redEdges and blueEdges where:
redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
Example 1:
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
Constraints:
1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
# Time - O(n)
# Space - O(n)

from collections import defaultdict, deque
from typing import List


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    red = defaultdict(list)
    blue = defaultdict(list)

    for src, dst, in redEdges:
        red[src].append(dst)

    for src, dst in blueEdges:
        blue[src].append(dst)

    answer = [-1 for i in range(n)]
    q = deque()
    q.append([0, 0, None]) # [node, length, prev_edge_color]
    visit = set()
    visit.add((0, None))
    while q:
        node, length, edgeColor = q.popleft()
        if answer[node] == -1:
            answer[node] = length
        
        if edgeColor != 'RED':
            for nei in red[node]:
                if (nei, "RED") not in visit:
                    visit.add((nei, "RED"))
                    q.append([nei, length + 1, "RED"])

        if edgeColor == 'BLUE':
            for nei in blue[node]:
                if (nei, "BLUE") not in visit:
                    visit.add((nei, "BLUE"))
                    q.append([nei, length + 1, "BLUE"])
    return answer

print(shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
print(shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))
