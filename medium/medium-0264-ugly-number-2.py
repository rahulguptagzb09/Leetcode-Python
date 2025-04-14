"""
https://leetcode.com/problems/ugly-number-ii/description/
264. Ugly Number II
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Constraints:
1 <= n <= 1690
Hint 1
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
Hint 2
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
Hint 3
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Hint 4
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""
# Time - O(nlogn or n)
# Space - O(n)

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # minHeap = [1]
        # visit = set()
        # factors = [2, 3, 5]
        # for i in range(n):
        #     num = heapq.heappop(minHeap)
        #     if i == n - 1:
        #         return num
        #     for f in factors:
        #         if num * f not in visit:
        #             visit.add(num * f)
        #             heapq.heappush(minHeap, num * f)

        nums = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            next_num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(next_num)
            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1
            if next_num == nums[i5] * 5:
                i5 += 1
        return nums[n - 1]

s = Solution()
print(s.nthUglyNumber(n = 10))
print(s.nthUglyNumber(n = 1))
