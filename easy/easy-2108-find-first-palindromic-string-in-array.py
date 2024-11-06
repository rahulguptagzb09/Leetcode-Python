"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
2108. Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
"""
# Time - O(n*m)
# Space - O(m or 1)

from typing import List


def firstPalindrome(words: List[str]) -> str:
    # for w in words:
    #     if w == w[::-1]:
    #         return w
    # return ""

    for w in words:
        l, r = 0, len(w) - 1
        while w[l] == w[r]:
            if l >= r:
                return w
            l, r = l + 1, r - 1
    return ""

print(firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
print(firstPalindrome(words = ["notapalindrome","racecar"]))
print(firstPalindrome(words = ["def","ghi"]))
