"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
Hint 1
We can figure out what target each subset must sum to. Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.
"""

# Time - O(k * 2^n)
# Space - O(n)

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, k, subset_sum):
            if k == 0:
                return True
            if subset_sum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if not used[j] or subset_sum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)


sol = Solution()
print(sol.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
print(sol.canPartitionKSubsets(nums=[1, 2, 3, 4], k=3))
