"""
https://leetcode.com/problems/meeting-rooms/description/
252. Meeting Rooms
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""
# Time - O(nlogn)
# Space - O(1)

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i : i[0])
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2  = intervals[i]
            if i1[1] > i2[0]:
                return False
        return True

sol = Solution()
print(sol.canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]))
print(sol.canAttendMeetings(intervals = [[7,10],[2,4]]))
