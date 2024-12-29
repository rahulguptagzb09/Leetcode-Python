"""
https://leetcode.com/problems/uncrossed-lines/description/
1035. Uncrossed Lines
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
Return the maximum number of connecting lines we can draw in this way.
Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
Constraints:
1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
Hint 1
Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?
"""
# Time - O( 2^(m+n) or n*m)
# Space - O(n*m or m)

from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    # Memoization
    # def dfs(i, j):
    #     if i == len(nums1) or j == len(nums2):
    #         return 0
    #     if (i, j) in dp:
    #         return dp[(i, j)]
    #     if nums1[i] == nums2[j]:
    #         dp[(i, j)] = 1 + dfs(i + 1, j + 1)
    #     else:
    #         dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
    #     return dp[(i, j)]
    # dp = {}
    # return dfs(0, 0)

    # Dynamic Programming
    prev = [0] * (len(nums2) + 1)
    for i in range(len(nums1)):
        dp = [0] * (len(nums2) + 1)
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[j + 1] = 1 + prev[j]
            else:
                dp[j + 1] = max(dp[j], prev[j + 1])
        prev = dp
    return dp[len(nums2)]

print(maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4]))
print(maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
print(maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]))
