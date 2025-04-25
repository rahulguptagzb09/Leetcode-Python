"""
https://leetcode.com/problems/minimum-time-difference/description/
539. Minimum Time Difference
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""
# Time - O(nlogn or n)
# Space - O(1)

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # def time_to_min(t):
        #     h, m = map(int, t.split(":"))
        #     return 60 * h + m
        # timePoints.sort()
        # res = 24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0])
        # for i in range(len(timePoints) - 1):
        #     cur = time_to_min(timePoints[i + 1])
        #     prev = time_to_min(timePoints[i])
        #     diff =  cur - prev
        #     res = min(res, diff)
        #     if res == 0:
        #         return 0
        # return res

        def time_to_min(t):
            h, m = map(int, t.split(":"))
            return 60 * h + m
        exists = [False] * (60 * 24)
        first_m, last_m = 60 * 24, 0
        for t in timePoints:
            m = time_to_min(t)
            if exists[m]:
                return 0
            exists[m] = True
            first_m = min(first_m, m)
            last_m = max(last_m, m)
        res = 60 * 24 - last_m + first_m
        prev_m = first_m
        for m in range(first_m + 1, len(exists)):
            if exists[m]:
                diff = m - prev_m
                res = min(res, diff)
                prev_m = m
        return res

sol = Solution()
print(sol.findMinDifference(timePoints = ["23:59","00:00"]))
print(sol.findMinDifference(timePoints = ["00:00","23:59","00:00"]))
