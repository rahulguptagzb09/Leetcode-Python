"""
https://leetcode.com/problems/maximum-sum-circular-subarray/
918. Maximum Sum Circular Subarray
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
Constraints:
n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Hint 1
For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
Hint 2
What is an alternate way of representing a circular array so that it appears to be a straight array? Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:
Hint 3
The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?
"""
# Time - O(n)
# Space - O(1)

from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    globMax, globMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0
    for n in nums:
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globMax = max(globMax, curMax)
        globMin = min(globMin, curMin)

    return max(globMax, total - globMin) if globMax > 0 else globMax

print(maxSubarraySumCircular(nums = [1,-2,3,-2]))
print(maxSubarraySumCircular(nums = [5,-3,5]))
print(maxSubarraySumCircular(nums = [-3,-2,-3]))
