"""
https://leetcode.com/problems/longest-palindrome/description/
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

def longestPalindrome(s: str) -> int:
    res = 0
    seen = set()

    for c in s:
        if c in seen:
            seen.remove(c)
            res += 2
        else:
            seen.add(c)
    return res + 1 if seen else res  

print(longestPalindrome(s = "abccccdd"))
print(longestPalindrome(s = "a"))