"""
https://leetcode.com/problems/squares-of-a-sorted-array/
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l]**2 > nums[r]**2:
                res.append(nums[l]**2)
                l += 1
            else:
                res.append(nums[r]**2)
                r -= 1
        return res[::-1] # reverse

sol = Solution()
print(sol.sortedSquares(nums = [-4,-1,0,3,10]))
print(sol.sortedSquares(nums = [-7,-3,2,3,11]))
