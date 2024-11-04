"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
974. Subarray Sums Divisible by K
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.
Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:
Input: nums = [5], k = 9
Output: 0
"""
# Time - O(n)
# Space - O(n)

from collections import defaultdict
from typing import List

def subarraysDivByK(nums: List[int], k: int) -> int:
    prefix_sum = 0
    res = 0
    prefix_cnt = defaultdict(int)
    prefix_cnt[0] = 1
    for n in nums:
        prefix_sum += n 
        remain = prefix_sum % k
        
        res += prefix_cnt[remain] 
        prefix_cnt[remain] += 1
    return res

print(subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
print(subarraysDivByK(nums = [5], k = 9))