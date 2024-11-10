"""
https://leetcode.com/problems/count-number-of-nice-subarrays/description/
1248. Count Number of Nice Subarrays
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2 
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
Hint 1
After replacing each even by zero and every odd by one can we use prefix sum to find answer ?
Hint 2
Can we use two pointers to count number of sub-arrays ?
Hint 3
Can we store the indices of odd numbers and for each k indices count the number of sub-arrays that contains them ?
"""
# Time - O(n)
# Space - O(1)

from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    res = 0
    odd = 0
    l, m= 0, 0
    for r in range(len(nums)):
        if nums[r] % 2:
            odd += 1
        
        while odd > k:
            if nums[l] % 2:
                odd -= 1
            l += 1
            m = 1
        if odd == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l)  + 1
    return res

print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
print(numberOfSubarrays(nums = [2,4,6], k = 1))
print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
