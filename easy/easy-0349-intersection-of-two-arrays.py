"""
https://leetcode.com/problems/intersection-of-two-arrays/description/
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their 
intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
# Time - O(n)
# Space - O(n)

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    seen = set(nums1)
    for n in nums2:
        if n in seen:
            res.append(n)
            seen.remove(n)
    return res

print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
