"""
https://leetcode.com/problems/maximum-swap/description/
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
Constraints:
0 <= num <= 108
"""
# Time - O(n)
# Space - O(1)

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_digit = "0"
        max_i = -1
        swap_i =  swap_j = -1
        for i in reversed(range(len(num))):
            # max
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            # swap
            if num[i] < max_digit:
                swap_i, swap_j = i, max_i
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int("".join(num))

sol = Solution()
print(sol.maximumSwap(num = 2736))
print(sol.maximumSwap(num = 9973))