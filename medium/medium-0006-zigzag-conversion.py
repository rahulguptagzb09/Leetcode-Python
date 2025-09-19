"""
https://leetcode.com/problems/zigzag-conversion/description/
6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:
Input: s = "A", numRows = 1
Output: "A"
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            inc = 2 * (numRows - 1)
            for i in range(r, len(s), inc):
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + inc - 2 * r < len(s)):
                    res += s[i + inc - 2 * r]
        return res

sol = Solution()
print(sol.convert(s = "PAYPALISHIRING", numRows = 3))
print(sol.convert(s = "PAYPALISHIRING", numRows = 4))
print(sol.convert(s = "A", numRows = 1))
