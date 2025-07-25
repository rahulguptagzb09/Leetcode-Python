"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
1760. Minimum Limit of Balls in a Ba
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.
You can perform the following operation at most maxOperations times:
Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.
Return the minimum possible penalty after performing the operations.
Example 1:
Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:
Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.
Constraints:
1 <= nums.length <= 105
1 <= maxOperations, nums[i] <= 109
Hint 1
Let's change the question if we know the maximum size of a bag what is the minimum number of bags you can make
Hint 2
note that as the maximum size increases the minimum number of bags decreases so we can binary search the maximum size
"""
# Time - O(n*m or n*logm)
# Space - O(1)

import math
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def can_divide(max_balls):
            ops = 0
            for n in nums:
                ops += math.ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True

        # for i in range(1, max(nums) + 1):
        #     if can_divide(i):
        #         return i

        l, r = 0, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if can_divide(m):
                r = m
            else:
                l = m + 1
        return l

sol = Solution()
print(sol.minimumSize(nums = [9], maxOperations = 2))
print(sol.minimumSize(nums = [2,4,8,2], maxOperations = 4))
