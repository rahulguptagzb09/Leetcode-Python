"""
https://leetcode.com/problems/word-pattern/description/
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".
Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
# Time - O(n+m)
# Space - O(n+m)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True

sol = Solution()
print(sol.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(sol.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(sol.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
