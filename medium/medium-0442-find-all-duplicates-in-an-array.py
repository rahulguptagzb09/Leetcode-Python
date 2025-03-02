"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:
Input: nums = [1,1,2]
Output: [1]
Example 3:
Input: nums = [1]
Output: []
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
# Time - O(n)
# Space - O(1)

from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            res.append(n)
        nums[n - 1] = -nums[n - 1]

    return res

print(findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(findDuplicates(nums = [1,1,2]))
print(findDuplicates(nums = [1]))