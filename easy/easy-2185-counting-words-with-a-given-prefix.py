"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/
2185. Counting Words With a Given Prefix
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.
Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
Constraints:
1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
Hint 1
Go through each word in words and increment the answer if pref is a prefix of the word.
"""
# Time - O(n*m)
# Space - O(m)

from typing import List

class PrefixNode:
    def __init__(self) -> None:
        self.children = {} # a -> PrefixNode
        self.count = 1

class PrefixTree:
    def __init__(self) -> None:
        self.root = PrefixNode()

    def add(self, w):
        cur = self.root
        for c in w:
            if cur not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
            cur.count += 1

    def count(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # n = len(pref)
        # res = 0
        # for w in words:
        #     if w[:n] == pref:
        #        res += 1
        # return res
        
        prefix_tree = PrefixTree()
        for w in words:
            if len(w) >= len(pref):
                prefix_tree.add(w)
        return prefix_tree.count(pref)

sol = Solution()
print(sol.prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))
print(sol.prefixCount(words = ["leetcode","win","loops","success"], pref = "code"))
