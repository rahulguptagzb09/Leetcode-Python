"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
# Time - O(n)
# Space - O(1)

from collections import defaultdict


def firstUniqChar(s: str) -> int:
    count = defaultdict(int)

    for c in s:
        count[c] += 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

print(firstUniqChar(s = "leetcode"))
print(firstUniqChar(s = "loveleetcode"))
print(firstUniqChar(s = "aabb"))
