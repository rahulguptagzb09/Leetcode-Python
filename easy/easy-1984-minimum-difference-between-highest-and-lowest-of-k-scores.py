"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
1984. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.
Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
Constraints:
1 <= k <= nums.length <= 1000
0 <= nums[i] <= 105
Hint 1
For the difference between the highest and lowest element to be minimized, the k chosen scores need to be as close to each other as possible.
Hint 2
What if the array was sorted?
Hint 3
After sorting the scores, any contiguous k scores are as close to each other as possible.
Hint 4
Apply a sliding window solution to iterate over each contiguous k scores, and find the minimum of the differences of all windows.
"""
# Time - O(nlogn)
# Space - O(1)

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res

sol = Solution()
print(sol.minimumDifference(nums = [90], k = 1))
print(sol.minimumDifference(nums = [9,4,1,7], k = 2))
