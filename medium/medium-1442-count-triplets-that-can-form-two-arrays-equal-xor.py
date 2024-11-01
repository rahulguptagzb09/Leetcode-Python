"""
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.
Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:
Input: arr = [1,1,1,1,1]
Output: 10
Hint 1
We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays so that the xor of the first array is equal to the xor of the second array. This is equivalent to searching for sub-array with xor = 0.
Hint 2
Keep the prefix xor of arr in another array, check the xor of all sub-arrays in O(n^2), if the xor of sub-array of length x is 0 add x-1 to the answer.
"""
# Time - O(n)
# Space - O(1)

from collections import defaultdict
from typing import List

def countTriplets(arr: List[int]) -> int:
    N = len(arr)
    res = 0
    prefix = 0
    prev_xor_cnt = defaultdict(int)
    prev_xor_cnt[0] = 1
    prev_xor_index_sum = defaultdict(int)

    for i in range(N):
        prefix ^= arr[i]

        if prev_xor_cnt[prefix]:
            res += i * prev_xor_cnt[prefix] - prev_xor_index_sum[prefix]

        prev_xor_cnt[prefix] += 1
        prev_xor_index_sum[prefix] += i + 1
    
    return res

print(countTriplets(arr = [2,3,1,6,7]))
print(countTriplets(arr = [1,1,1,1,1]))