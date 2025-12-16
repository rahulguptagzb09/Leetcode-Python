"""
https://leetcode.com/problems/reverse-linked-list-ii/description/
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
Follow up: Could you do it in one pass?
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # reach node at position at left
        left_prev, cur = dummy, head
        for _ in range(left - 1):
            left_prev, cur = cur, cur.next
        # now cur = left, left_prev = node before left
        # reverse from left to right
        prev = None
        for _ in range(right - left + 1):
            temp_next = cur.next
            cur.next = prev
            prev, cur = cur, temp_next
        # update pointers
        left_prev.next.next = cur # cur is node after right
        left_prev.next = prev # prev is right
        return dummy.next
