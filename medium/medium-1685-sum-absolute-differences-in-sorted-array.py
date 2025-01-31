"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/
1685. Sum of Absolute Differences in a Sorted Array
You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
Example 1:
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
Constraints:
2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
Hint 1
Absolute difference is the same as max(a, b) - min(a, b). How can you use this fact with the fact that the array is sorted?
Hint 2
For nums[i], the answer is (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i-1]) + (nums[i+1] - nums[i]) + (nums[i+2] - nums[i]) + ... + (nums[n-1] - nums[i]).
Hint 3
It can be simplified to (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) + ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1)). One can build prefix and suffix sums to compute this quickly.
"""
# Time - O(n)
# Space - O(1)

from typing import List


def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    total_sum = sum(nums)
    left_sum = 0
    res = []
    for i, n in enumerate(nums):
        rigt_sum = total_sum - n - left_sum
        left_size, right_size = i, len(nums) - i - 1
        res.append(left_size * n - left_sum + rigt_sum - right_size * n)
        left_sum += n

    return res

print(getSumAbsoluteDifferences(nums = [2,3,5]))
print(getSumAbsoluteDifferences(nums = [1,4,6,8,10]))
