"""
https://leetcode.com/problems/binary-subarrays-with-sum/description/
930. Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
Constraints:
1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""
# Time - O(n)
# Space - O(1)


from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:

    # Count num of sub arrays where curSum <= x
    def helper(x):
        if x < 0:
            return 0
        res = 0
        l, cur = 0, 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur > x:
                cur -= nums[l]
                l += 1
            res += (r - l + 1)
        return res
    return helper(goal) - helper(goal - 1)

print(numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
print(numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))
