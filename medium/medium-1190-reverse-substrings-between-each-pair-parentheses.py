"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
1190. Reverse Substrings Between Each Pair of Parentheses
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
Example 1:
Input: s = "(abcd)"
Output: "dcba"
Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Constraints:
1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
Hint 1
Find all brackets in the string.
Hint 2
Does the order of the reverse matter ?
Hint 3
The order does not matter.
"""
# Time - O(n^2 or n)
# Space - O(n)

def reverseParentheses(s: str) -> str:
    # stack = []
    # for c in s:
    #     if c == ")":
    #         portion = []
    #         while stack[-1] != "(":
    #             portion.append(stack.pop())
    #         stack.pop()
    #         stack.extend(portion)
    #     else:
    #         stack.append(c)
    # return "".join(stack)

    pair = {}
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            j = stack.pop()
            pair[i] = j
            pair[j] = i
    i, direction = 0, 1
    res = []
    while i < len(s):
        if s[i] == "(" or s[i] == ")":
            i = pair[i]
            direction = -direction
        else:
            res.append(s[i])
        i += direction
    return "".join(res)

print(reverseParentheses(s = "(abcd)"))
print(reverseParentheses(s = "(u(love)i)"))
print(reverseParentheses(s = "(ed(et(oc))el)"))
