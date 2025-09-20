"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
1930. Unique Length-3 Palindromic Subsequences
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
Constraints:
3 <= s.length <= 105
s consists of only lowercase English letters.
Hint 1
What is the maximum number of length-3 palindromic strings?
Hint 2
How can we keep track of the characters that appeared to the left of a given position?
"""
# Time - O(n)
# Space - O(n)

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set() # (mid_c, outer_c)
        left = set()
        right = Counter(s)
        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((m, c))
            left.add(m)
        return len(res)

sol = Solution()
print(sol.countPalindromicSubsequence(s = "aabca"))
print(sol.countPalindromicSubsequence(s = "adc"))
print(sol.countPalindromicSubsequence(s = "bbcbaba"))
