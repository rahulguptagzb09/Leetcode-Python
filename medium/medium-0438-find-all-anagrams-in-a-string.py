"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
# Time - O(n)
# Space - O(n)

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count, s_count = {}, {}
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
        res = [0] if s_count == p_count else []
        l = 0
        for r in range(len(p), len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                s_count.pop(s[l])
            l += 1
            if s_count == p_count:
                res.append(l)
        return res

sol = Solution()
print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))
print(sol.findAnagrams(s = "abab", p = "ab"))
