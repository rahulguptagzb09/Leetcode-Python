"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
884. Uncommon Words from Two Sentences
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.
Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
# Time - O(n+m)
# Space - O(n+m)

from collections import Counter, defaultdict
from typing import List


def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    # count = defaultdict(int)
    # for w in s1.split(" ") + s2.split(" "):
    #     count[w] += 1
    # res = []
    # for w, cnt in count.items():
    #     if cnt == 1:
    #         res.append(w)
    # return res
    
    return [w for w, cnt in Counter(s1.split(" ") + s2.split(" ")).items() if cnt == 1]

print(uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
