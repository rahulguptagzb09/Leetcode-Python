"""
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/
2563. Count the Number of Fair Pairs
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
Constraints:
1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
Hint 1
Sort the array in ascending order.
Hint 2
For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.
Hint 3
As you move to larger number, both boundaries move down.
"""
# Time - O(nlogn)
# Space - O(1)

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def bin_search(l, r, target):
            # Return largest i where nums[i] < target
            while l <= r:
                m = (l + r) // 2 # (r - l) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r
   
        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (bin_search(i + 1, len(nums) - 1, up + 1) - bin_search(i + 1, len(nums) - 1, low))

        return res

sol = Solution()
print(sol.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
print(sol.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))
