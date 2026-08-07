"""
https://leetcode.com/problems/reorganize-string/
767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
Example 1:
Input: s = "aab"
Output: "aba"
Example 2:
Input: s = "aaab"
Output: ""
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
Hint 1
Alternate placing the most common letters.
"""

# Time - O(nlogn)
# Space - O(n)

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # char -> count
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            # most freq char except prev
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res


sol = Solution()
print(sol.reorganizeString(s="aab"))
print(sol.reorganizeString(s="aaab"))
