"""
https://leetcode.com/problems/excel-sheet-column-title/description/
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1:
Input: columnNumber = 1
Output: "A"
Example 2:
Input: columnNumber = 28
Output: "AB"
Example 3:
Input: columnNumber = 701
Output: "ZY"
Constraints:
1 <= columnNumber <= 231 - 1
"""
# Time - O(log n)

def convertToTitle(columnNumber: int) -> str:
    res = ""
    while columnNumber > 0:
        offset = (columnNumber - 1) % 26
        res += chr(ord('A') + offset)
        columnNumber = (columnNumber - 1) // 26
    
    return res[::-1] # reverse 

print(convertToTitle(columnNumber = 1))
print(convertToTitle(columnNumber = 28))
print(convertToTitle(columnNumber = 701))
