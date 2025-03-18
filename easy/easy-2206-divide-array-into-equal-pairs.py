"""
https://leetcode.com/problems/divide-array-into-equal-pairs/
2206. Divide Array Into Equal Pairs
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
Constraints:
nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
Hint 1
For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.
Hint 2
The elements with equal value can be divided completely into pairs if and only if their count is even.
"""
# Time - O(n)
# Space - O(n)

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # count = {}
        # for n in nums:
        #     if n not in count:
        #         count[n] = 0
        #     count[n] += 1
        # for n, cnt in count.items():
        #     if cnt % 2:
        #         return False
        # return True

        odd_set = set()
        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)
        return len(odd_set) == 0

sol = Solution()
print(sol.divideArray(nums = [3,2,3,2,2,2]))
print(sol.divideArray(nums = [1,2,3,4]))