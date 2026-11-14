"""
https://leetcode.com/problems/meeting-rooms-ii/
https://leetcode.ca/2016-08-09-253-Meeting-Rooms-II/
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

# Time - O(nlogn)
# Space - O(n)

from typing import List


class Interval(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Intervals
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


solution = Solution()
intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print("Example 1 Output:", solution.minMeetingRooms(intervals1))
intervals2 = [Interval(7, 10), Interval(2, 4)]
print("Example 2 Output:", solution.minMeetingRooms(intervals2))
