"""
https://leetcode.com/problems/majority-element/description/
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
# Time - O(n)
# Space - O(n or 1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # res, max_count = 0, 0
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > max_count else res
        #     max_count = max(count[n], max_count)
        # return res

        # Boyer-Moore Voting
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))
