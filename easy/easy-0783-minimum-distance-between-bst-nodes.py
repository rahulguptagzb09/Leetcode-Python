"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
783. Minimum Distance Between BST Nodes
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1
        4
    2       6
1       3
Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
    1
0       48
    12      49
Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
# Time - O(n)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res


        