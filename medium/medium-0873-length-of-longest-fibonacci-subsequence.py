"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
873. Length of Longest Fibonacci Subsequence
A sequence x1, x2, ..., xn is Fibonacci-like if:
n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
Constraints:
3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
"""
# Time - O(n^2 * logn or n^2)
# Space - O(n or n^2)

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # arr_set = set(arr)
        # res = 0
        # for i in range(len(arr) - 1):
        #     for j in range(i + 1, len(arr)):
        #         prev, cur = arr[i], arr[j]
        #         nxt = prev + cur
        #         length = 2
        #         while nxt in arr_set:
        #             length += 1
        #             prev, cur = cur, nxt
        #             nxt = prev + cur
        #         res = max(res, length)
        # return res

        res = 0
        arr_map = {n:i for i, n in enumerate(arr)}
        dp = [[0] * len(arr) for _ in range(len(arr))] # (i, j) -> length of longest subseq
        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i + 1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                res = max(res, length)
                dp[i][j] = length
        return res

sol = Solution()
print(sol.lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))
print(sol.lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))
