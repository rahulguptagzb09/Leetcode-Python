"""
https://leetcode.com/problems/permutations/description/
46. Permutations
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
# Time - O(n! * n^2)
# Space - O(n! * n^2)

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    perms = [[]]
    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(p_copy)
        perms = new_perms
    return perms

print(permute(nums = [1,2,3]))
print(permute(nums = [0,1]))
print(permute(nums = [1]))
