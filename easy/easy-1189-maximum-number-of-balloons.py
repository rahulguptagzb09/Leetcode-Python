"""
https://leetcode.com/problems/maximum-number-of-balloons/description/
1189. Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
Example 1:
Input: text = "nlaebolko"
Output: 1
Example 2:
Input: text = "loonbalxballpoon"
Output: 2
Example 3:
Input: text = "leetcode"
Output: 0
Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.
Note: This question is the same as 2287: Rearrange Characters to Make Target String.
Hint 1
Count the frequency of letters in the given string.
Hint 2
Find the letter than can make the minimum number of instances of the word "balloon".
"""
# Time - O(n)
# Space - O(n)

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        balloon = Counter("balloon")
        res = len(text) # or float("inf")
        for c in balloon:
            res = min (res, count_text[c] // balloon[c])
        return res

sol = Solution()
print(sol.maxNumberOfBalloons(text = "nlaebolko"))
print(sol.maxNumberOfBalloons(text = "loonbalxballpoon"))
print(sol.maxNumberOfBalloons(text = "leetcode"))
