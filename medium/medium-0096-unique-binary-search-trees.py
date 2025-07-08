"""
https://leetcode.com/problems/unique-binary-search-trees/description/
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
Constraints:
1 <= n <= 19
"""
# Time - O(n^2)
# Space - O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        # numTree[4] = numTree[0] * numtree[3] + 
        #              numTree[1] * numtree[2] + 
        #              numTree[2] * numtree[1] + 
        #              numTree[3] * numtree[1]
        numTree = [1] * (n + 1)
        # 0 node = 1 tree
        # 1 node = 1 tree
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

sol = Solution()
print(sol.numTrees(n = 3))
print(sol.numTrees(n = 1))
