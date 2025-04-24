"""
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
1371. Find the Longest Substring Containing Vowels in Even Counts
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
Example 1:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
Constraints:
1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
Hint 1
Represent the counts (odd or even) of vowels with a bitmask.
Hint 2
Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # vowels = "aeiou"
        # res = 0
        # mask = 0
        # mask_to_idx = {0: -1}
        # for i, c in enumerate(s):
        #     if c in vowels:
        #         mask = mask ^ (1 + ord(c) - ord('a'))
        #     if mask in mask_to_idx:
        #         length = i - mask_to_idx[mask]
        #         res = max(res, length)
        #     else:
        #         mask_to_idx[mask] = i
        # return res

        vowels = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        res = 0
        mask = 0
        mask_to_idx = [-1] * 32
        for i, c in enumerate(s):
            mask = mask ^ vowels.get(c, 0)
            if mask_to_idx[mask] != -1 or mask == 0:
                length = i - mask_to_idx[mask]
                res = max(res, length)
            else:
                mask_to_idx[mask] = i
        return res


sol = Solution()
print(sol.findTheLongestSubstring(s = "eleetminicoworoep"))
print(sol.findTheLongestSubstring(s = "leetcodeisgreat"))
print(sol.findTheLongestSubstring(s = "bcbcbc"))
