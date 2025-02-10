"""
https://leetcode.com/problems/sum-of-subarray-minimums/description/
907. Sum of Subarray Minimums
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
# Time - O(n)
# Space  - O(n)

from typing import List


def sumSubarrayMins(arr: List[int]) -> int:
    MOD = 10**9 + 7
    res = 0
    stack = [] # (index, num)
    for i, n in enumerate(arr):
        while stack and n < stack[-1][1]:
            j, m = stack.pop()
            left = j - stack[-1][0] if stack else j + 1
            right = i - j
            res = (res + m * left * right) % MOD
        stack.append((i, n))
    
    for i in range(len(stack)):
        j, n = stack[i]
        left = j - stack[i - 1][0] if i > 0 else j + 1
        right = len(arr) - j
        res = (res + n * left * right) % MOD

    return res

print(sumSubarrayMins(arr = [3,1,2,4]))
print(sumSubarrayMins(arr = [11,81,94,43,3]))
