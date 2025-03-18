"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
You are given an integer array nums.
In one move, you can choose one element of nums and change it to any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:
Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
Hint 1
The minimum difference possible is obtained by removing three elements between the three smallest and three largest values in the array.
"""
# Time - O(nlogn or n)
# Space - O(1)


import heapq
from typing import List


def minDifference(nums: List[int]) -> int:
    # if len(nums) <= 4:
    #     return 0
    # nums.sort()
    # res = float("inf")
    # for l in range(4):
    #     r = len(nums) - 4 + l
    #     res = min(res, nums[r] - nums[l])
    # return res

    if len(nums) <= 4:
        return 0
    min_four = sorted(heapq.nsmallest(4, nums))
    max_four = sorted(heapq.nlargest(4, nums))
    res = float("inf")
    for i in range(4):
        res = min(res, max_four[i] - min_four[i])
    return res

print(minDifference(nums = [5,3,2,4]))
print(minDifference(nums = [1,5,0,10,14]))
print(minDifference(nums = [3,100,20]))
