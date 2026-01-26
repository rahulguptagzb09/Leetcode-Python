"""
https://leetcode.com/problems/largest-number/
179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
Example 1:
Input: nums = [10,2]
Output: "210"
Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
# Time - O(nlogn)
# Space - O(n)

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))

sol = Solution()
print(sol.largestNumber(nums = [10,2]))
print(sol.largestNumber(nums = [3,30,34,5,9]))
