"""
https://leetcode.com/problems/number-of-good-pairs/description/
1512. Number of Good Pairs
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:
Input: nums = [1,2,3]
Output: 0
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
# Time - O(n)


from collections import Counter
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    # count = Counter(nums) # n -> c
    # res = 0
    # for n,c in count.items():
    #     res += c * (c - 1) // 2
    # return res

    count = {}
    res = 0
    for n in nums:
        if n in count:
            res += count[n]
            count[n] += 1
        else:
            count[n] = 1
    return res


print(numIdenticalPairs(nums = [1,2,3,1,1,3]))
print(numIdenticalPairs(nums = [1,1,1,1]))
print(numIdenticalPairs(nums = [1,2,3]))
