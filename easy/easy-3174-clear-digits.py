"""
https://leetcode.com/problems/clear-digits/
3174. Clear Digits
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.
Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".
Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
Hint 1
Process string s from left to right, if s[i] is a digit, mark the nearest unmarked non-digit index to its left.
Hint 2
Delete all digits and all marked characters.
"""
# Time - O(n)
# Space - O(n)

class Solution:
    def clearDigits(self, s: str) -> str:
        # res = []
        # del_cnt = 0
        # for i in reversed(range(len(s))):
        #     # if s[i].isdigit():
        #     if ord("0") <= ord(s[i]) <= ord("9"):
        #         del_cnt += 1
        #     elif del_cnt:
        #         del_cnt -= 1
        #     else:
        #         res.append(s[i])
        # return "".join(res[::-1])

        res = []
        for i in range(len(s)):
            if ord("0") <= ord(s[i]) <= ord("9"):
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)

sol = Solution()
print(sol.clearDigits(s = "abc"))
print(sol.clearDigits(s = "cb34"))
