"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
1721. Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
Hint 1
We can traverse the linked list and store the elements in an array.
Hint 2
Upon conversion to an array, we can swap the required elements by indexing the array.
Hint 3
We can rebuild the linked list using the order of the elements in the array.
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for i in range(k - 1):
            cur = cur.next

        left = cur
        right = head
        while cur.next:
            cur = cur.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head
