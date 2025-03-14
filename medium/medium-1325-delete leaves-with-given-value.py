"""
https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
1325. Delete Leaves With a Given Value
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Constraints:
The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
Hint 1
Use the DFS to reconstruct the tree such that no leaf node is equal to the target. If the leaf node is equal to the target, return an empty object instead.
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
        
def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    # Recursive 
    # if not root:
    #     return None
    # root.left = removeLeafNodes(root.left, target)
    # root.right = removeLeafNodes(root.right, target)
    # if not root.left and not root.right and root.val == target:
    #     return None
    # return root

    # Interative
    stack = [root]
    visit = set()
    parents = { root : None }
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            if node.val == target:
                p = parents[node]
                if not p:
                    return None
                if p.left == node:
                    p.left = None
                if p.right == node:
                    p.right = None
        elif node not in visit:
            visit.add(node)
            stack.append(node)
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
    return root 


# print(removeLeafNodes(root = [1,2,3,2,null,2,4], target = 2))
# print(removeLeafNodes(root = [1,3,3,3,2], target = 3))
# print(removeLeafNodes(root = [1,2,null,2,null,2], target = 2))

