"""
https://leetcode.com/problems/can-place-flowers/description/
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
# Time - O(n)
# Space - O(n or 1)

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # f = [0] + flowerbed + [0]
        # for i in range(1, len(f) - 1): # skip first and last
        #     if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
        #         f[i] = 1
        #         n -= 1
        # return n <= 0

        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2) # int division, round toward zero
                empty = 0
            else:
                empty += 1
        n -= (empty) // 2
        return n <= 0

sol = Solution()
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
