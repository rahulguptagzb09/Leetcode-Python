"""
https://leetcode.com/problems/remove-nodes-from-linked-list/description/
2487. Remove Nodes From Linked List
You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.
Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
Constraints:
The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
Hint 1
Iterate on nodes in reversed order.
Hint 2
When iterating in reversed order, save the maximum value that was passed before.
"""
# Time - O(n)
# Space - O(n or 1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack = []
        # cur = head
        # while cur:
        #     while stack and cur.val > stack[-1]:
        #         stack.pop()
        #     stack.append(cur.val)
        #     cur = cur.next
        # dummy = ListNode()
        # cur = dummy
        # for n in stack:
        #     cur.next = ListNode(n)
        #     cur = cur.next
        # return dummy.next

        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev
        head = reverse(head)
        cur = head
        cur_max = cur
        while cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next
        return reverse(head)
