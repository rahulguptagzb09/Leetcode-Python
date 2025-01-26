"""
https://leetcode.com/problems/validate-binary-tree-nodes/
1361. Validate Binary Tree Nodes
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
Note that the nodes have no values and that we only use the node numbers in this problem.
Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Constraints:
n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
Hint 1
Find the parent of each node.
Hint 2
A valid tree must have nodes with only one parent and exactly one node with no parent.
"""
# Time - O(n)
# Space - O(n)

from typing import List


def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    hasParent = set(leftChild + rightChild)
    hasParent.discard(-1)
    if len(hasParent) == n:
        return False
    root = -1
    for i in range(n):
        if i not in hasParent:
            root = i
            break
    visit = set()
    def dfs(i):
        if i == -1:
            return True
        if i in visit:
            return False
        visit.add(i)
        return dfs(leftChild[i]) and dfs(rightChild[i])
    
    return dfs(root) and len(visit) == n

print(validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
print(validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
print(validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))
