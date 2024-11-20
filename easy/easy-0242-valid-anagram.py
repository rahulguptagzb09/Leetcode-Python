"""
https://leetcode.com/problems/valid-anagram/
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
# Time - O(s+t + nlogn)
# Space - O(s+t + 1)

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True
    
        # return Counter(s) == Counter(t)

        return sorted(s) == sorted(t)

sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "rat", t = "car"))
