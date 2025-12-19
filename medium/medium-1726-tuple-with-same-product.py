"""
https://leetcode.com/problems/tuple-with-same-product/
1726. Tuple with Same Product
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
Hint 1
Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
Hint 2
Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.
"""
# Time - O(n^2)
# Space - O(n)

from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # product_cnt = defaultdict(int) # n1 * n2 - count
        # pair_cnt = defaultdict(int) # n1 * n2 - count if pairs (a, b) and (c, d)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         product = nums[i] * nums[j]
        #         pair_cnt[product] += product_cnt[product]
        #         product_cnt[product] += 1
        # res = 0
        # for cnt in pair_cnt.values():
        #     res += 8 * cnt
        # return res

        product_cnt = defaultdict(int) # n1 * n2 - count
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_cnt[product] += 1
        res = 0
        for cnt in product_cnt.values():
            pairs = (cnt * (cnt - 1)) // 2
            res += 8 * pairs
        return res

sol = Solution()
print(sol.tupleSameProduct(nums = [2,3,4,6]))
print(sol.tupleSameProduct(nums = [1,2,4,5,10]))
