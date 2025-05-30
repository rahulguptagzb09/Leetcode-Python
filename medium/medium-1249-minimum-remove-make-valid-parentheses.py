"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Constraints:
1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
Hint 1
Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.
Hint 2
Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.
"""
# Time - O(n)
# Space - O(n)

def minRemoveToMakeValid(s: str) -> str:
    res = []
    cnt = 0 # extra ( parentheses
    for c in s:
        if c == "(":
            res.append(c)
            cnt += 1
        elif c == ")" and cnt > 0:
            res.append(c)
            cnt -= 1
        elif c!= ")":
            res.append(c)
    filtered = []
    for c in res[::-1]:
        if c == "(" and cnt > 0:
            cnt -= 1
        else:
            filtered.append(c)
    return "".join(filtered[::-1])

print(minRemoveToMakeValid(s = "lee(t(c)o)de)"))
print(minRemoveToMakeValid(s = "a)b(c)d"))
print(minRemoveToMakeValid(s = "))(("))
