"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
1508. Range Sum of Sorted Subarray Sums
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
Example 1:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
Example 2:
Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
Example 3:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50
Constraints:
n == nums.length
1 <= nums.length <= 1000
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2
Hint 1
Compute all sums and save it in array.
Hint 2
Then just go from LEFT to RIGHT index and calculate answer modulo 1e9 + 7.
"""
# Time - O(n^2 * logn)
# Space - O(n^2 or n)

import heapq
from typing import List


def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    # MOD = 10 ** 9 + 7
    # subarr_sum = []
    # for i in range(n):
    #     cur_sum = 0
    #     for j in range(i, n):
    #         cur_sum = (cur_sum + nums[j]) % MOD
    #         subarr_sum.append(cur_sum)
    # subarr_sum.sort()
    # res = 0
    # for i in range(left - 1, right):
    #     res = (res + subarr_sum[i]) % MOD
    # return res

    MOD = 10 ** 9 + 7
    minHeap = [(n, i) for i, n in enumerate(nums)]
    heapq.heapify(minHeap)
    res = 0
    for i in range(right):
        num, index = heapq.heappop(minHeap)
        if i >= left - 1:
            res = (res + num) % MOD
        if index + 1 < n:
            next_pair = (num + nums[index + 1], index + 1)
            heapq.heappush(minHeap, next_pair)
    return res

print(rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
print(rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
print(rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))
