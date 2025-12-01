"""
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
1437. Check If All 1's Are at Least Length K Places Away
Easy
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Constraints:
1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
Hint 1
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.
"""

# Time - O(n)
# Space - O(1)

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = k
        for n in nums:
            if n == 1:
                if res < k:
                    return False
                res = 0
            else:
                res += 1
        return True


sol = Solution()
print(sol.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(sol.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
