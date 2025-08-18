"""
https://leetcode.com/problems/best-sightseeing-pair/description/
1014. Best Sightseeing Pair
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots.
Example 1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:
Input: values = [1,2]
Output: 2
Constraints:
2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
Hint 1
Can you tell the best sightseeing spot in one pass (ie. as you iterate over the input?) What should we store or keep track of as we iterate to do this?
"""
# Time - O(n)
# Space - O(1)
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        cur_max = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, values[i] + cur_max)
            cur_max = max(cur_max - 1, values[i] - 1)
        return res

sol = Solution()
print(sol.maxScoreSightseeingPair(values = [8,1,5,2,6]))
print(sol.maxScoreSightseeingPair(values = [1,2]))
