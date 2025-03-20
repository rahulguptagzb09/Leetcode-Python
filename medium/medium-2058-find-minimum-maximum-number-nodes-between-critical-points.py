"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.
Constraints:
The number of nodes in the list is in the range [2, 105].
1 <= Node.val <= 105
Hint 1
The maximum distance must be the distance between the first and last critical point.
Hint 2
For each adjacent critical point, calculate the difference and check if it is the minimum distance.
"""
# Time - O(n)
# Space - O(1)

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev, cur, nxt):
            return prev.val > cur.val < nxt.val or prev.val < cur.val > nxt.val
        
        prev, cur = head, head.next
        nxt = cur.next
        min_dist, max_dist = float("inf"), -1
        prev_crit_idx = 0
        first_crit_idx = 0
        i = 1 # index of cur
        while nxt:
            if critical(prev, cur, nxt):
                if first_crit_idx:
                    max_dist = i - first_crit_idx
                    min_dist = min(min_dist, i - prev_crit_idx)
                else:
                    first_crit_idx = i
                prev_crit_idx = i
            prev, cur, nxt = cur, nxt, nxt.next
            i += 1
        if min_dist == float("inf"):
            min_dist = -1
            
        return [min_dist, max_dist]
