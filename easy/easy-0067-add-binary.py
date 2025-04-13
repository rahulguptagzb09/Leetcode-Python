"""
https://leetcode.com/problems/add-binary/
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord('0') if i < len(a) else 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digit_a + digit_b + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        if carry:
            res = "1" + res
        return res

sol = Solution()
print(sol.addBinary(a = "11", b = "1"))
print(sol.addBinary(a = "1010", b = "1011"))
