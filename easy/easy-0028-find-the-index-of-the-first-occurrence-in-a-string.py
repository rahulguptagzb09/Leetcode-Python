"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
# Time - O(n*m or n+m)
# Space - O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == "":
        #     return 0
        # for i in range(len(haystack) + 1 - len(needle)):
        #     if haystack[i: i + len(needle)] == needle:
        #         return i
        # return -1

        # Knuth–Morris–Pratt KMP
        if needle == "":
            return 0
        lps = [0] * len(needle)
        prev_lps, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1

sol = Solution()
print(sol.strStr(haystack = "sadbutsad", needle = "sad"))
print(sol.strStr(haystack = "leetcode", needle = "leeto"))
