"""
https://leetcode.com/problems/multiply-strings/
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

# Time - O(n*m)
# Space - O(n+m)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Math and Geometry
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1, n1 in enumerate(num1):
            for i2, n2 in enumerate(num2):
                digit = int(n1) * int(n2)
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        res, begin = res[::-1], 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        res = map(str, res[begin:])
        return "".join(res)


sol = Solution()
print(sol.multiply(num1="2", num2="3"))
print(sol.multiply(num1="123", num2="456"))
