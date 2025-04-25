"""
https://leetcode.com/problems/search-in-a-binary-search-tree/description/
700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
# Time - O(n or n)
# Space - O(n or 1)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursion
        # if not root or root.val == val:
        #     return root
        # return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

        # Iteration
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

# Create the example trees
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)

# Create the solution instance
solution = Solution()

# Run the examples
result1 = solution.searchBST(root1, 2)
result2 = solution.searchBST(root2, 5)

# Print the results directly
def print_result(node: Optional[TreeNode]):
    if not node:
        print("[]")
    else:
        result = []
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        print(result)

print("Example 1 Output:", end=" ")
print_result(result1)

print("Example 2 Output:", end=" ")
print_result(result2)
