"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/
979. Distribute Coins in Binary Tree
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.
Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
Constraints:
The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
"""
# Time - O(n)
# Space - O(h)

# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distributeCoins(root: TreeNode) -> int:
    # res = 0
    # def dfs(cur):
    #     if not(cur):
    #         return [0, 0] # [size, coins]
    #     l_size, l_coins = dfs(cur.left)
    #     r_size, r_coins = dfs(cur.right)
    #     size = 1 + l_size + r_size
    #     coins = cur.val + l_coins + r_coins
    #     res += abs(size - coins)
    #     return [size, coins]
    # dfs(root)
    # return res
    
    res = 0
    def dfs(cur):
        if not(cur):
            return 0 # extra coins
        l_extra = dfs(cur.left)
        r_extra = dfs(cur.right)
        extra_coins = cur.val - 1 + l_extra + r_extra
        res += abs(extra_coins)
        return extra_coins
    dfs(root)
    return res

# print(distributeCoins(root = [3,0,0]))
# print(distributeCoins(root = [0,3,0]))
