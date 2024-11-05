"""
https://leetcode.com/problems/set-mismatch/description/
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:
Input: nums = [1,1]
Output: [1,2]
Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
# Time - O(n)
# Space - O(n or 1 or 1)

from typing import Counter, List


def findErrorNums(nums: List[int]) -> List[int]:
    # res = [0, 0] # [duplicate, missing]
    # count = Counter(nums)
    # for i in range(1, len(nums) + 1):
    #     if count[i] == 0:
    #         res[1] = i
    #     if count[i] == 2:
    #         res[0] = i
    # return res
    
    # res = [0, 0] # [duplicate, missing]
    # for n in nums:
    #     n = abs(n)
    #     nums[n - 1] = -nums[n - 1]
    #     if nums[n - 1] > 0:
    #         res[0] = n
    # for i, n in enumerate(nums):
    #     if n > 0 and i + 1 != res[0]:
    #         res[1] = i + 1
    #         return res

    N = len(nums)
    x = 0 # duplicate - missing
    y = 0 # duplicat^2 - missing^2
    for i in range(1, N+1):
        x += nums[i - 1] - i
        y += nums[i - 1]**2 - i**2
    missing = (y - x**2) // (2 * x)
    duplicate = missing + x 
    return [duplicate, missing]

print(findErrorNums(nums = [1,2,2,4]))
print(findErrorNums(nums = [1,1]))
