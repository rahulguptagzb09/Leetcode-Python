"""
https://leetcode.com/problems/minimize-xor/
2429. Minimize XOR
Given two positive integers num1 and num2, find the positive integer x such that:
x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.
Return the integer x. The test cases are generated such that x is uniquely determined.
The number of set bits of an integer is the number of 1's in its binary representation.
Example 1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
Constraints:
1 <= num1, num2 <= 109
Hint 1
To arrive at a small xor, try to turn off some bits from num1
Hint 2
If there are still left bits to set, try to set them from the least significant bit
"""
# Time - O(logn)
# Space - O(1)

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        def count_bits(n):
            res = 0
            while n > 0:
                res += 1 & n
                n  = n >> 1
            return res

        count_1, count_2 = count_bits(num1), count_bits(num2)
        x = num1
        i = 0
        while count_1 != count_2:
            # Remove least significant bit
            if count_1 > count_2 and x & (1 << i):
                count_1 -= 1
                x = x ^ (1 << i)
            # Adding least soignificant bit 
            if count_1 < count_2 and x & (1 << i) == 0:
                count_1 += 1
                x = x | (1 << i)
            i += 1

        return x

sol = Solution()
print(sol.minimizeXor(num1 = 3, num2 = 5))
print(sol.minimizeXor(num1 = 1, num2 = 12))
