"""
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
1780. Check if Number is a Sum of Powers of Three
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
An integer y is a power of three if there exists an integer x such that y == 3x.
Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:
Input: n = 21
Output: false
Constraints:
1 <= n <= 107
Hint 1
Let's note that the maximum power of 3 you'll use in your soln is 3^16
Hint 2
The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it
"""
# Time - O(n or logn)
# Space - O(n or 1)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # def backtrack(i, cur):
        #     if cur == n:
        #         return True
        #     if cur > n or 3**i > n:
        #         return False
        #     # include
        #     if backtrack(i + 1, cur + 3**i):
        #         return True
        #     # skip
        #     return backtrack(i + 1, cur)
        # return backtrack(0, 0)

        # find largest power of 3^i <= n
        i = 0
        while 3**(i+1) <= n:
            i += 1
        # greedy, remove the largest powers
        while i>= 0:
            power = 3**i
            if power <= n:
                n -= power
            if power <= n:
                return False
            i -= 1
        return n == 0

sol = Solution()
print(sol.checkPowersOfThree(n = 12))
print(sol.checkPowersOfThree(n = 12))
print(sol.checkPowersOfThree(n = 21))
