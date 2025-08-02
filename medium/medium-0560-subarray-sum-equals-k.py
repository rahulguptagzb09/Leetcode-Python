"""
https://leetcode.com/problems/subarray-sum-equals-k/
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
Hint 1
Will Brute force work here? Try to optimize it.
Hint 2
Can we optimize it by using some extra space?
Hint 3
What about storing sum frequencies in a hash table? Will it be useful?
Hint 4
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
"""
# Time - O(n)
# Space - O(n)

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sum = { 0:1 }
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        return res

sol = Solution()
print(sol.subarraySum(nums = [1,1,1], k = 2))
print(sol.subarraySum(nums = [1,2,3], k = 3))
