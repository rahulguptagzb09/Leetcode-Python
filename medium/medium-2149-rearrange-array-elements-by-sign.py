"""
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
2149. Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
Constraints:
2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.
It is not required to do the modifications in-place.
Hint 1
Divide the array into two parts- one comprising of only positive integers and the other of negative integers.
Hint 2
Merge the two parts to get the resultant array.
"""
# Time - O(n)
# Space - O(n)

from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
    # pos, neg = [], []
    # for n in nums:
    #     if n > 0:
    #         pos.append(n)
    #     else:
    #         neg.append(n)
    # i = 0
    # while 2 * i < len(nums):
    #     nums[2 * i] = pos[i]
    #     nums[2 * i + 1] = neg[i]
    #     i += 1
    # return nums

    i, j = 0, 1
    res = [0] * len(nums)
    k = 0
    for k in range(len(nums)):
        if nums[k] > 0:
            res[i] = nums[k]
            i += 1
        else:
            res[j] = nums[k]
            j += 2
    return res

print(rearrangeArray(nums = [3,1,-2,-5,2,-4]))
print(rearrangeArray(nums = [-1,1]))
