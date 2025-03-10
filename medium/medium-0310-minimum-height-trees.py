"""
https://leetcode.com/problems/minimum-height-trees/description/
310. Minimum Height Trees
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Constraints:
1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
Hint 1
How many MHTs can a graph have at most?
"""
# Time - O(n^2)
# Space - O(n)

from collections import defaultdict, deque
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    edge_cnt = {}
    leaves = deque()
    for src, neighbors in adj.items():
        if len(neighbors) == 1:
            leaves.append(src)
        edge_cnt[src] = len(neighbors)
    while leaves:
        if n <= 2:
            return list(leaves)
        for i in range(len(leaves)):
            node = leaves.popleft()
            n -= 1
            for nei in adj[node]:
                edge_cnt[nei] -= 1
                if edge_cnt[nei] == 1:
                    leaves.append(nei)

print(findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
