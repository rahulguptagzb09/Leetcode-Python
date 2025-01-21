"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
1658. Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
Hint 1
Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
Hint 2
Finding the maximum subarray is standard and can be done greedily.
"""
# Time - O(n)
# Space - O(1)

from typing import List


def minOperations(nums: List[int], x: int) -> int:
    target = sum(nums) - x
    cur_sum = 0
    max_window = -1
    l = 0
    for r in range(len(nums)):
        cur_sum += nums[r]
        while l <= r and cur_sum > target:
            cur_sum -= nums[l]
            l += 1
        if cur_sum == target:
            max_window = max(max_window, r - l + 1)
        
    return -1 if max_window == -1 else len(nums) - max_window

print(minOperations(nums = [1,1,4,2,3], x = 5))
print(minOperations(nums = [5,6,7,8,9], x = 4))
print(minOperations(nums = [3,2,20,1,1,3], x = 10))
