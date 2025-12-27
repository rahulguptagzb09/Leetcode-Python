"""
https://leetcode.com/problems/partition-labels/
763. Partition Labels
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.
Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:
Input: s = "eccbbbbdec"
Output: [10]
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
Hint 1
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {} # char -> last index in s
        for i, c in enumerate(s):
            last_index[c] = i
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                res.append(size)
                size = 0
        return res

sol = Solution()
print(sol.partitionLabels(s = "ababcbacadefegdehijhklij"))
print(sol.partitionLabels(s = "eccbbbbdec"))
