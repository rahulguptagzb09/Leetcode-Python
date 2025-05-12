"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
1545. Find Kth Bit in Nth Binary String
Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
Constraints:
1 <= n <= 20
1 <= k <= 2n - 1
Hint 1
Since n is small, we can simply simulate the process of constructing S1 to Sn.
"""
# Time - O(n)
# Space - O(n)

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1

        # def helper(length, k, invert):
        #     if length == 1:
        #         return "0" if not invert else "1"
        #     half = length // 2
        #     if k <= half:
        #         return helper(half, k, invert)
        #     elif k > half + 1:
        #         return helper(half, 1 + length - k, not invert)
        #     else:
        #         return "1" if not invert else "0"
        # return helper(length, k, False)

        invert = False
        while length > 1:
            half = length // 2
            if k <= half:
                length = half
            elif k > half + 1:
                k = 1 + length - k
                length = half
                invert = not invert
            else:
                return "1" if not invert else "0"
        return "0" if not invert else "1"

sol = Solution()
print(sol.findKthBit(n = 3, k = 1))
print(sol.findKthBit(n = 4, k = 11))
