"""
https://leetcode.com/problems/majority-element-ii/description/
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:
Input: nums = [3,2,3]
Output: [3]
Example 2:
Input: nums = [1]
Output: [1]
Example 3:
Input: nums = [1,2]
Output: [1,2]
Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
Follow up: Could you solve the problem in linear time and in O(1) space?
Hint 1
Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
Hint 2
It can be at most two. Why?
Hint 3
Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.
"""
# Time - O(n)
# Space - O(1)

from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> List[int]:
    count = defaultdict(int)
    
    for n in nums:
        count[n] += 1

        if len(count) <= 2:
            continue    
        new_count = defaultdict(int)
        for n, c in count.items():
            if c > 1:
                new_count[n] = c - 1
        count = new_count
    res = []
    for n in count:
        if nums.count(n) > len(nums) // 3:
            res.append(n)
    return res

print(majorityElement(nums = [3,2,3]))
print(majorityElement(nums = [1]))
print(majorityElement(nums = [1,2]))
