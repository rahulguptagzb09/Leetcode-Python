"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
2616. Minimize the Maximum Difference of Pairs
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2
Hint 1
Can we use dynamic programming here?
Hint 2
To minimize the answer, the array should be sorted first.
Hint 3
The recurrence relation is fn(i, x) = min(fn(i+1, x), max(abs(nums[i]-nums[i+1]), fn(i+2, p-1)), and fn(0,p) gives the desired answer.
"""
# Time - O(nlogm)
# Space = O(nlogm)

from typing import List


def minimizeMax(nums: List[int], p: int) -> int:
    
    def isValid(threshold):
        # Greedy
        i, cnt = 0, 0 
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= threshold:
                cnt += 1
                i += 2
            else:
                i += 1
            if cnt == p:
                return True
        return False

    if p == 0:
        return 0
    nums.sort()
    l, r = 0, 10**9
    res = 10**9
    while l <= r:
        m = l + (r - l) // 2 # (l + r) // 2
        if isValid(m):
            res = m 
            r = m - 1
        else:
            l = m + 1
    return res

print(minimizeMax(nums = [10,1,2,7,1,3], p = 2))
print(minimizeMax(nums = [4,2,1,2], p = 1))
