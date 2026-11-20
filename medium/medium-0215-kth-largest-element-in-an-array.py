"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

# Time - O(nlogn or n^2)
# Space - O(n or 1)

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap Priority Queue
        # Sorting nlogn
        # nums.sort()
        # return nums[len(nums) - k]

        # Quick Select n^2
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick_select(l, p - 1)
            if p < k:
                return quick_select(p + 1, r)
            return nums[p]

        return quick_select(0, len(nums) - 1)


sol = Solution()
print(sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
