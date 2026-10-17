"""
https://leetcode.com/problems/longest-repeating-character-replacement/
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

# Time - O(n)
# Space - O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        char_count = {}
        res = 0
        l = 0
        max_freq = 0
        for r, c_r in enumerate(s):
            char_count[c_r] = 1 + char_count.get(c_r, 0)
            max_freq = max(max_freq, char_count[c_r])
            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


sol = Solution()
print(sol.characterReplacement(s="ABAB", k=2))
print(sol.characterReplacement(s="AABABBA", k=1))
