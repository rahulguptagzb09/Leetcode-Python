"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""
# Time - O(n*k + m)
# Space - O(n+m)

from collections import Counter, defaultdict
from typing import List


def countCharacters(words: List[str], chars: str) -> int:
    res = 0
    count = Counter(chars)
    for w in words:
        cur_word = defaultdict(int)
        good = True
        for c in w:
            cur_word[c] += 1
            if c not in count or cur_word[c] > count[c]:
                good = False
                break
        if good:
            res += len(w)
    return res

print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
