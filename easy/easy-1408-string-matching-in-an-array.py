"""
https://leetcode.com/problems/string-matching-in-an-array/
1408. String Matching in an Array
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string
Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
Hint 1
Bruteforce to find if one string is substring of another or use KMP algorithm.
"""
# Time - O(n^2 * l^2)
# Space - O(1)

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i  == j:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

sol = Solution()
print(sol.stringMatching(words = ["mass","as","hero","superhero"]))
print(sol.stringMatching(words = ["leetcode","et","code"]))
print(sol.stringMatching(words = ["blue","green","bu"]))
