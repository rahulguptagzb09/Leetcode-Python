"""
https://leetcode.com/problems/contains-duplicate-ii/description/
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
# Time - O(n)
# Space - O(k)

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()
    L = 0
    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
