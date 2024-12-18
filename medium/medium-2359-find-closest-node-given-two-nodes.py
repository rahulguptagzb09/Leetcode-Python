"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
2359. Find Closest Node to Given Two Nodes
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
You are also given two integers node1 and node2.
Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.
Note that edges may contain cycles.
Example 1:
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
Constraints:
n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
"""
# Time - O(n)
# Space - O(n)

from collections import defaultdict, deque
from typing import List


def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    adj = defaultdict(list)
    for i, dst in enumerate(edges):
        adj[i].append(dst)
    
    def bfs(src, distMap):
        q = deque()
        q.append([src, 0])
        distMap[src] = 0
        while q:
            node, dist = q.popleft()
            for nei in adj[node]:
                if nei not in distMap:
                    q.append([nei, dist + 1])
                    distMap[nei] = dist + 1

    node1Dist = {} # Map node -> distance from node1
    node2Dist = {} # Map node -> distance from node2
    bfs(node1, node1Dist)
    bfs(node2, node2Dist)

    res = -1
    resDist = float("inf")
    for i in range(len(edges)):
        if i in node1Dist and i in node2Dist:
            dist = max(node1Dist[i], node2Dist[i])
            if dist < resDist:
                res = i
                resDist = dist
    return res

print(closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))
