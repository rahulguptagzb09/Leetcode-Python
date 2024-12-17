"""
https://leetcode.com/problems/reverse-string/
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""
# Time - O(n)
# Space - O(1 or n or n)

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l, r = 0, len(s) - 1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r - 1
        # return s

        # stack = []
        # for c in s:
        #     stack.append(c)
        # i = 0
        # while stack:
        #     s[i] = stack.pop()
        #     i += 1
        # return s

        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s) - 1)
        return s

sol = Solution()
print(sol.reverseString(s = ["h","e","l","l","o"]))
print(sol.reverseString(s = ["H","a","n","n","a","h"]))
