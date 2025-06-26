"""
https://leetcode.com/problems/permutations-ii/description/
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
# Time - O(n*2^n)
# Space - O(n)

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = { n:0 for n in nums }
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()

        dfs()
        return res

sol = Solution()
print(sol.permuteUnique(nums = [1,1,2]))
print(sol.permuteUnique(nums = [1,2,3]))
