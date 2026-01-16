"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
1524. Number of Sub-arrays With Odd Sum
Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.
Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16
Constraints:
1 <= arr.length <= 105
1 <= arr[i] <= 100
Hint 1
Can we use the accumulative sum to keep track of all the odd-sum sub-arrays ?
Hint 2
if the current accu sum is odd, we care only about previous even accu sums and vice versa.
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        odd_cnt, even_cnt = 0, 0
        res = 0
        mod = 10**9 + 7
        for n in arr:
            cur_sum += n
            if cur_sum % 2: # odd
                res = (res + 1 + even_cnt) % mod
                odd_cnt += 1
            else: # even
                res = (res + odd_cnt) % mod
                even_cnt += 1
        return res

sol = Solution()
print(sol.numOfSubarrays(arr = [1,3,5]))
print(sol.numOfSubarrays(arr = [2,4,6]))
print(sol.numOfSubarrays(arr = [1,2,3,4,5,6,7]))
