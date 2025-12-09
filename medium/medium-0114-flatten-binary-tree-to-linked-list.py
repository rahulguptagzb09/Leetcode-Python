"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [0]
Output: [0]
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
Hint 1
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""
# Time - O(n)
# Space - O(n)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # flatten the root tree and return list tail
        def dfs(root):
            if not root:
                return None
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)
            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            last = right_tail or left_tail or root
            return last

        dfs(root)
