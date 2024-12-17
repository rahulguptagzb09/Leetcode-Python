"""
https://leetcode.com/problems/valid-palindrome-ii/description/
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:
Input: s = "abc"
Output: false
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l + 1:r + 1], s[l:r]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            l, r = l + 1, r - 1
        return True

sol = Solution()
print(sol.validPalindrome(s = "aba"))
print(sol.validPalindrome(s = "abca"))
print(sol.validPalindrome(s = "abc"))
