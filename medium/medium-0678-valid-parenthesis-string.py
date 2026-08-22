"""
https://leetcode.com/problems/valid-parenthesis-string/
678. Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "(*)"
Output: true
Example 3:
Input: s = "(*))"
Output: true
Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
Hint 1
Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
Hint 2
DP[i][j] represents whether the substring s[i:j] is valid.
Hint 3
Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
Hint 4
How about using 2 stacks instead of 1? Think about it.
"""

# Time - O(n)
# Space - O(1)


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Greedy
        left_max, left_min = 0, 0
        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            if left_max < 0:
                return False
            left_min = max(left_min, 0)  # s = ( * ) (
        return left_min == 0


sol = Solution()
print(sol.checkValidString(s="()"))
print(sol.checkValidString(s="(*)"))
print(sol.checkValidString(s="(*))"))
