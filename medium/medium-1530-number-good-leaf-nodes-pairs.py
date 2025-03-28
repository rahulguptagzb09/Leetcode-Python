"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
1530. Number of Good Leaf Nodes Pairs
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.
Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
    1
2       3
    4
Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
            1
    2               3
4       5       6       7
Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
Constraints:
The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
Hint 1
Start DFS from each leaf node. stop the DFS when the number of steps done > distance.
Hint 2
If you reach another leaf node within distance steps, add 1 to the answer.
Hint 3
Note that all pairs will be counted twice so divide the answer by 2.
"""
# Time - O(n^3)
# Space - O(n)

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # self.pairs = 0
        # def dfs(node):
        #     if not node:
        #         return []
        #     if not node.left and not node.right:
        #         return [1]
        #     left_dist = dfs(node.left)
        #     right_dist = dfs(node.right)
        #     for d1 in left_dist:
        #         for d2 in right_dist:
        #             if d1 + d2 <= distance:
        #                 self.pairs += 1
        #     all_dist = left_dist + right_dist
        #     return [d + 1 for d in all_dist]
        # dfs(root)
        # return self.pairs

        self.pairs = 0
        def dfs(node):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)
            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.pairs += left_dist[d1] * right_dist[d2]
            all_dist = defaultdict(int)
            for d in left_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] = left_dist[d] 
            for d in right_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] += right_dist[d] 
            return all_dist
        dfs(root)
        return self.pairs
