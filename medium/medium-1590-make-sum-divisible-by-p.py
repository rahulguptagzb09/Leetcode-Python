"""
https://leetcode.com/problems/make-sum-divisible-by-p/
1590. Make Sum Divisible by P
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.
Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109
Hint 1
Use prefix sums to calculate the subarray sums.
Hint 2
Suppose you know the remainder for the sum of the entire array. How does removing a subarray affect that remainder? What remainder does the subarray need to have in order to make the rest of the array sum up to be divisible by k?
Hint 3
Use a map to keep track of the rightmost index for every prefix sum % p.
"""

# Time - O(n)
# Space - O(n)

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        if remain == 0:
            return 0
        res = len(nums)
        cur_sum = 0
        remain_to_index = {0: -1}  # remain of prefix sums -> last index
        for i, n in enumerate(nums):
            # x = cur_sum - remain
            cur_sum = (n + cur_sum) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_index:
                length = i - remain_to_index[prefix]
                res = min(res, length)
            remain_to_index[cur_sum] = i
        return -1 if res == len(nums) else res


sol = Solution()
print(sol.minSubarray(nums=[3, 1, 4, 2], p=6))
print(sol.minSubarray(nums=[6, 3, 5, 2], p=9))
print(sol.minSubarray(nums=[1, 2, 3], p=3))
