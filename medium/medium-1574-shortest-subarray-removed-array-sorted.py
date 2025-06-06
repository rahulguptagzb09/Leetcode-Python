"""
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
1574. Shortest Subarray to be Removed to Make Array Sorted
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.
Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
Constraints:
1 <= arr.length <= 105
0 <= arr[i] <= 109
Hint 1
The key is to find the longest non-decreasing subarray starting with the first element or ending with the last element, respectively.
Hint 2
After removing some subarray, the result is the concatenation of a sorted prefix and a sorted suffix, where the last element of the prefix is smaller than the first element of the suffix.
"""
# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # # Remove prefix
        # N = len(arr)
        # r = N - 1
        # while r > 0 and arr[r - 1] <= arr[r]:
        #     r -= 1
        # res = r
        # # Remove postfix
        # l = 0
        # while l + 1 < N and arr[l] <= arr[l + 1]:
        #     l += 1
        # res = min(res, N - 1 - l)
        # # Remove middle
        # l, r = 0, N - 1
        # while l < r:
        #     # Shrink valid window
        #     while r < N and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
        #         r -= 1
        #     # Expand invalid window
        #     while r < N and arr[l] > arr[r]:
        #         r += 1
        #     res = min(res, r - l - 1)
        #     if arr[l] > arr[l + 1]:
        #         break
        #     l += 1
        # return res
        
        # Remove prefix
        N = len(arr)
        r = N - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = r
        # Remove postfix / middle
        l = 0
        while l < r:
            # Expand invalid window
            while r < N and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        return res

sol = Solution()
print(sol.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]))
print(sol.findLengthOfShortestSubarray(arr = [5,4,3,2,1]))
print(sol.findLengthOfShortestSubarray(arr = [1,2,3]))
