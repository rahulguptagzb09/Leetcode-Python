"""
https://leetcode.com/problems/swap-nodes-in-pairs/
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Explanation:
Example 2:
Input: head = []
Output: []
Example 3:
Input: head = [1]
Output: [1]
Example 4:
Input: head = [1,2,3]
Output: [2,1,3]
Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Time - O(n)
# Space - O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save pointers
            next_pair = curr.next.next
            second = curr.next
            # reverse pair
            second.next = curr
            curr.next = next_pair
            prev.next = second
            # update pointers
            prev = curr
            curr = next_pair
        return dummy.next
