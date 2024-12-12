"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Hint 1
This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think counters!
Hint 2
However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.
Hint 3
The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

sol = Solution()
print(sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbers(nums = [1,1]))
