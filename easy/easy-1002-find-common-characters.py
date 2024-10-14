"""
https://leetcode.com/problems/find-common-characters/description/
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

from collections import Counter
from typing import List

def commonChars(words: List[str]) -> List[str]:
    cnt = Counter(words[0])
    for w in words:
        cur_cnt = Counter(w)
        for c in cnt:
            cnt[c] = min(cnt[c], cur_cnt[c])

    res = []
    for c in cnt:
        for i in range(cnt[c]):
            res.append(c)

    return res

print(commonChars(words = ["bella","label","roller"]))
print(commonChars(words = ["cool","lock","cook"]))