"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:
Input: root = [1,2,3]
Output: [1,3]
Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""
# Time - O(n)
# Space - O(n)

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            row_max = q[0].val
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row_max)
        return res
