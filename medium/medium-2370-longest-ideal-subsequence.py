"""
https://leetcode.com/problems/longest-ideal-subsequence/description/
2370. Longest Ideal Subsequence
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
Constraints:
1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.
Hint 1
How can you calculate the longest ideal subsequence that ends at a specific index i?
Hint 2
Can you calculate it for all positions i? How can you use previously calculated answers to calculate the answer for the next position?
"""
# Time - O(n or 1)
# Space - O(n)


def longestIdealString(s: str, k: int) -> int:
    # cache = {}
    # def helper(i, prev):
    #     if i == len(s):
    #         return 0
    #     if (i, prev) in cache:
    #         return cache[(i, prev)]
    #     res = helper(i + 1, prev) # skip s[i]
    #     if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
    #         res = max(res, 1 + helper(i + 1, s[i])) # include s[i]
    #     cache[(i, prev)] = res
    #     return res
    # return helper(0, "")

    # Dynamic Programming
    dp = [0] * 26
    for c in s:
        curr = ord(c) - ord('a') # 0 - 25
        longest = 1
        for prev in range(26):
            if abs(curr - prev) <= k:
                longest = max(longest, 1 + dp[prev])
        dp[curr] = max(dp[curr], longest)
    return max(dp)

print(longestIdealString(s = "acfgbd", k = 2))
print(longestIdealString(s = "abcd", k = 3))
