"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
1624. Largest Substring Between Two Equal Characters
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.
Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.
"""
# Time - O(n)
# Space - O(1)

def maxLengthBetweenEqualCharacters(s: str) -> int:
    char_index = {} # char -> first index
    res = -1
    for i, c in enumerate(s):
        if c in char_index:
            res = max(res, i - char_index[c] - 1)
        else:
            char_index[c] = i
    return res

print(maxLengthBetweenEqualCharacters(s = "aa"))
print(maxLengthBetweenEqualCharacters(s = "abca"))
print(maxLengthBetweenEqualCharacters(s = "cbzxy"))
