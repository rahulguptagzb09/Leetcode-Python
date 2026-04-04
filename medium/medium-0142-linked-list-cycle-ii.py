"""
https://leetcode.com/problems/linked-list-cycle-ii/
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Time - O(n)
# Space - O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

# Function to get the index of the cycle start node
def get_cycle_start_index(head: ListNode, cycle_start_node: ListNode) -> int:
    index = 0
    current = head
    while current != cycle_start_node:
        current = current.next
        index += 1
    return index


# Example 1: head = [3, 2, 0, -4], pos = 1
head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Create cycle

# Example 2: head = [1, 2], pos = 0
head2 = ListNode(1)
node2_2 = ListNode(2)
head2.next = node2_2
node2_2.next = head2  # Create cycle

# Example 3: head = [1], pos = -1
head3 = ListNode(1)
# No cycle

# Run the function
solution = Solution()
result1 = solution.detectCycle(head1)
result2 = solution.detectCycle(head2)
result3 = solution.detectCycle(head3)

# Print results with clearer output
print(
    f"Example 1: tail connects to node index {get_cycle_start_index(head1, result1) if result1 else 'no cycle'}"
)
print(
    f"Example 2: tail connects to node index {get_cycle_start_index(head2, result2) if result2 else 'no cycle'}"
)
print(
    f"Example 3: {'no cycle' if result3 is None else f'tail connects to node index {get_cycle_start_index(head3, result3)}'}"
)
