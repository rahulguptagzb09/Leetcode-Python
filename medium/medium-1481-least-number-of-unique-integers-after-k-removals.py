"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
1481. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements. 
Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
Hint 1
Use a map to count the frequencies of the numbers in the array.
Hint 2
An optimal strategy is to remove the numbers with the smallest count first.
"""
# Time - O(nlogn or n)
# Space - O(n)

from collections import Counter
import heapq
from typing import List


def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    # freq = Counter(arr)
    # heap = list(freq.values())
    # heapq.heapify(heap)
    # res = len(heap)
    # while k > 0 and heap:
    #     f = heapq.heappop(heap)
    #     if k >= f:
    #         k -= f
    #         res -= 1
    # return res

    freq = Counter(arr)
    freq_list = [0] * (len(arr) + 1) # freq -> no of elements w that freq
    for n, f in freq.items():
        freq_list[f] += 1
    res = len(freq)
    for f in range(1, len(freq_list)):
        remove = freq_list[f]
        if k >= f * remove:
            k -= f * remove
            res -= remove
        else:
            remove = k // f
            res -= remove
            break
    return res

print(findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
print(findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))
