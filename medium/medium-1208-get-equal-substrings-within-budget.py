"""
https://leetcode.com/problems/get-equal-substrings-within-budget/
1208. Get Equal Substrings Within Budget
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.
Hint 1
Calculate the differences between s[i] and t[i].
Hint 2
Use a sliding window to track the longest valid substring.
"""
# Time - O(n)
# Space - O(1)

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    res = 0
    curCost = 0
    l = 0
    for r in range(len(s)):
        curCost += abs(ord(s[r]) - ord(t[r]))
        while curCost > maxCost:
            curCost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        res = max(res, r-l+1)
    return res

print(equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
print(equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
print(equalSubstring(s = "abcd", t = "acde", maxCost = 0))