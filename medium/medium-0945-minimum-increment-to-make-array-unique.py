"""
https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
945. Minimum Increment to Make Array Unique
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.
Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
# Time - O(nlogn) quicksort or O(n) counting sort
# Space - O(n)

from collections import Counter
from typing import List

def minIncrementForUnique(nums: List[int]) -> int:
    # nums.sort()
    # res = 0
    # for i in range(1, len(nums)):
    #     if nums[i - 1] >= nums[i]:
    #         res += 1 + nums[i -1] - nums[i]
    #         nums[i] = nums[i - 1] + 1

    count = Counter(nums)
    res = 0
    for i in range(len(nums) + max(nums)):
        if count[i] > 1:
            extra = count[i] - 1
            count[i + 1] += extra
            res += extra
    return res

print(minIncrementForUnique(nums = [1,2,2]))
print(minIncrementForUnique(nums = [3,2,1,2,1,7]))
