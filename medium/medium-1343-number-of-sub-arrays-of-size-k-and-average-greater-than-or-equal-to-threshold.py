"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
Constraints:
1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
"""
# Time - O(n)
# Space - O(1)


from typing import List


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    res = 0
    curSum = sum(arr[0:k-1])
    for L in range(len(arr) - k + 1):
        curSum += arr[L + k - 1]
        if (curSum / k) >= threshold:
            res += 1
        curSum -= arr[L]

    return res

print(numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
