"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
https://leetcode.ca/2016-10-09-314-Binary-Tree-Vertical-Order-Traversal/
314. Binary Tree Vertical Order Traversal
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Time - O(n)
# Space - O(n)

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)]) # (node, col)
        min_col, max_col = 0, 0
        cols = defaultdict(list) # col index -> list of values
        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [cols[c] for c in range(min_col, max_col + 1)]

# Example 1: Input: root = [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Example 2: Input: root = [3,9,8,4,0,1,7]
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(8)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(0)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(7)

# Example 3: Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
root3 = TreeNode(3)
root3.left = TreeNode(9)
root3.right = TreeNode(8)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(0)
root3.right.left = TreeNode(1)
root3.right.right = TreeNode(7)
root3.left.right.right = TreeNode(2)  # Corrected position for node with value 2
root3.right.left.left = TreeNode(5)  # Corrected position for node with value 5

# Create Solution instance
solution = Solution()

# Run examples
print(solution.verticalOrder(root1))  # Output: [[9],[3,15],[20],[7]]
print(solution.verticalOrder(root2))  # Output: [[4],[9],[3,0,1],[8],[7]]
print(solution.verticalOrder(root3))  # Output: [[4],[9,5],[3,0,1],[8,2],[7]]
