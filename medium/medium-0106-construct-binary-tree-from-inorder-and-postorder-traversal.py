"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
        3
    9       20
        15      7
Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
# Time - O(n^2 or n)
# Space - O(n)

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # if not inorder:
        #     return None
        # root = TreeNode(postorder.pop())
        # idx = inorder.index(root.val)
        # root.right = self.buildTree(inorder[idx+1:], postorder)
        # root.left = self.buildTree(inorder[:idx], postorder)
        # return root

        inorderIdx = {v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)
            return root

        return helper(0, len(inorder) - 1)
    
