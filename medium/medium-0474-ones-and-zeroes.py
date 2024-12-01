"""
https://leetcode.com/problems/ones-and-zeroes/description/
474. Ones and Zeroes
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.
Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
# Time - O(m*n*s)
# Space - O(m*n*s)

from collections import defaultdict
from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    # # Memorization
    # dp = {}
    # def dfs(i, m, n):
    #     if i == len(strs):
    #         return 0
    #     if (i, m, n) in dp:
    #         return dp[(i, m, n)]
        
    #     mCnt, nCnt = strs[i].count("0"), strs[i].count("1")

    #     dp[(i, m, n)] = dfs(i + 1, m, n)
    #     if mCnt <= m and nCnt <= n:
    #         dp[(i, m, n)] = max(dfs(i, m, n), 1 + dfs(i + 1, m - mCnt, n - nCnt))
    #     return dp[(i, m, n)]
    # return dfs(0, m, n)

    # Dynamic Programming
    # dp = defaultdict(int)
    # for i in range(len(strs)):
    #     s = strs[i]
    #     mCnt, nCnt = s.count("0"), s.count("1")
    #     for M in range(0, m + 1):
    #         for N in range(0, n + 1):
    #             if mCnt <= M and nCnt <= N:
    #                         dp[(i, M, N)] = max(dp[(i - 1, M, N)], 1 + dp[(i - 1, M - mCnt, N - nCnt)])
    #             else:
    #                  dp[(i, M, N)] = dp[(i - 1, M, N)]
    # return dp[(len(strs) - 1, m, n)]

    # Dynamic Programming
    dp = defaultdict(int)
    for s in strs:
        mCnt, nCnt = s.count("0"), s.count("1")
        for M in range(m, mCnt - 1, -1):
            for N in range(n, nCnt - 1, -1):
                dp[(M, N)] = max(dp[(M, N)], 1 + dp[(M - mCnt, N - nCnt)])
    return dp[(m, n)]

print(findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(findMaxForm(strs = ["10","0","1"], m = 1, n = 1))
