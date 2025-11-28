"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
2002. Maximum Product of the Length of Two Palindromic Subsequences
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.
Return the maximum possible product of the lengths of the two palindromic subsequences.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
Example 1:
example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
Example 2:
Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
Example 3:
Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
Constraints:
2 <= s.length <= 12
s consists of lowercase English letters only.
Hint 1
Could you generate all possible pairs of disjoint subsequences?
Hint 2
Could you find the maximum length palindrome in each subsequence for a pair of disjoint subsequences?
"""
# Time - O(2^n)
# Space - O(2^n)

class Solution:
    def maxProduct(self, s: str) -> int:
        N, pali = len(s), {} # bitmask -> len
        for mask in range(1, 1 << N): # 1 << N == 2 ** N
            subseq = ""
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0: # disjoint
                    res = max(res, pali[m1] * pali[m2])
        return res

sol = Solution()
print(sol.maxProduct(s = "leetcodecom"))
print(sol.maxProduct(s = "bb"))
print(sol.maxProduct(s = "accbcaxxcxx"))
