"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
1239. Maximum Length of a Concatenated String with Unique Characters
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
Hint 1
You can try all combinations and keep mask of characters you have.
Hint 2
You can use DP.
"""
# Time - O(2^n * (m+k))
# Space - O(n)

from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def overlap(char_set, s):
            c = Counter(char_set) + Counter(s)
            return max(c.values()) > 1
            # prev = set()
            # for c in s:
            #     if c in char_set or c in prev:
            #         return True
            #     prev.add(c)
            # return False

        def backtrack(i):
            if i == len(arr):
                return len(char_set)
            res = 0
            if not overlap(char_set, arr[i]):
                for c in arr[i]:
                    char_set.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    char_set.remove(c)
            return max(res, backtrack(i + 1))  # dont concatenate arr[i]

        return backtrack(0)

sol = Solution()
print(sol.maxLength(arr = ["un","iq","ue"]))
print(sol.maxLength(arr = ["cha","r","act","ers"]))
print(sol.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))
