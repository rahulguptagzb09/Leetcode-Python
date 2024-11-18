"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
1684. Count the Number of Consistent Strings
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
Constraints:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
Hint 1
A string is incorrect if it contains a character that is not allowed
Hint 2
Constraints are small enough for brute force
"""
# Time - O(n*m)
# Space - O(1)

from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    # allowed = set(allowed)
    # res = len(words)
    # for w in words:
    #     for c in w:
    #         if c not in allowed:
    #             res -= 1
    #             break
    # return res

    bit_mask = 0
    for c in allowed:
        bit = 1 << (ord(c) - ord('a'))
        bit_mask = bit_mask | bit
    res = len(words)
    for w in words:
        for c in w:
            bit = 1 << (ord(c) - ord('a'))
            if bit & bit_mask == 0:
                res -= 1
                break
    return res

print(countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
