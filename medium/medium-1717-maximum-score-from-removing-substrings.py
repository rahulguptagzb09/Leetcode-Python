"""
https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
1717. Maximum Score From Removing Substrings
You are given a string s and two integers x and y. You can perform two types of operations any number of times.
Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
Constraints:
1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
Hint 1
Note that it is always more optimal to take one type of substring before another
Hint 2
You can use a stack to handle erasures
"""
# Time - O(n)
# Space - O(n)

def maximumGain(s: str, x: int, y: int) -> int:

    def remove_pairs(pair, score):
        nonlocal s
        res = 0
        stack = []
        for c in s:
            if c == pair[1] and stack and stack[-1] == pair[0]:
                stack.pop()
                res += score
            else:
                stack.append(c)
        s = "".join(stack)
        return res
    
    res = 0
    pair = "ab" if x > y else "ba"
    res += remove_pairs(pair, max(x, y))
    res +=  remove_pairs(pair[::-1], min(x, y))
    return res

print(maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
print(maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))
