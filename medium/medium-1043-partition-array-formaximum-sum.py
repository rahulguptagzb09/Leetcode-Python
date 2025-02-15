"""
https://leetcode.com/problems/partition-array-for-maximum-sum/description/
1043. Partition Array for Maximum Sum
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:
Input: arr = [1], k = 1
Output: 1
Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
Hint 1
Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
Hint 2
For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .
"""
# Time - O(n*k)
# Space - O(n)

from typing import List

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    # Memoization Recursion
    # cache = {}
    # def dfs(i):
    #     if i in cache:
    #         return cache[i]   
    #     curr_max = 0
    #     res = 0
    #     for j in range(i, min(len(arr), i + k)):
    #         curr_max = max(curr_max, arr[j])
    #         window_size = j - i + 1
    #         res = max(res, dfs(j + 1) + curr_max * window_size)
    #     cache[i] = res
    #     return res
    # return dfs(0)

    # Dynamic Programming
    dp = [0] * k
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        curr_max = 0
        max_at_i = 0
        for j in range(i, i - k, -1):
            if j < 0:
                break
            curr_max = max(curr_max, arr[j])
            window_size = i - j + 1
            curr_sum = curr_max * window_size
            sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
            max_at_i = max(max_at_i, curr_sum + sub_sum)
        dp[i % k] = max_at_i
    return dp[(len(arr) - 1) % k]

print(maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))
print(maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))
print(maxSumAfterPartitioning(arr = [1], k = 1))
