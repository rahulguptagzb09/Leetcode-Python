"""
https://leetcode.com/problems/extra-characters-in-a-string/description/
2707. Extra Characters in a String
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.
Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.
Example 2:
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
Constraints:
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
Hint 1
Can we use Dynamic Programming here?
Hint 2
Define DP[i] as the min extra character if breaking up s[0:i] optimally.
"""
# Time - O(n^3)
# Space - O(n)

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

def minExtraChar(s: str, dictionary: List[str]) -> int:
    # words = set(dictionary)
    dp = { len(s): 0 }
    trie = Trie(dictionary).root

    def dfs(i):
        if i in dp:
            return dp[i]
        
        res = 1 + dfs(i + 1) # skip curr char
        curr = trie        
        for j in range(i, len(s)):
            # if s[i:j+1] in words:
            #     res = min(res, dfs(j + 1))
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]
            if curr.word:    
                res = min(res, dfs(j + 1))
        dp[i] = res
        return res
    return dfs(0)

print(minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
print(minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))
