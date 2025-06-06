"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
921. Minimum Add to Make Parentheses Valid
A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
Example 1:
Input: s = "())"
Output: 1
Example 2:
Input: s = "((("
Output: 3
Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        res = 0
        for c in s:
            if c == "(":
                open_cnt += 1
            else:
                open_cnt -= 1
                if open_cnt < 0:
                    open_cnt = 0
                    res += 1
        return res + open_cnt

sol = Solution()
print(sol.minAddToMakeValid(s = "())"))
print(sol.minAddToMakeValid(s = "((("))
