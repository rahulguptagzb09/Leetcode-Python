"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
1822. Sign of the Product of an Array
There is a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
Constraints:
1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""
# Time - O(n)
# Space - O(1)

from typing import List


def arraySign(nums: List[int]) -> int:
    neg = 0
    for n in nums:
        if n == 0:
            return 0
        neg += (1 if n < 0 else 0)
    return -1 if neg % 2 else 1


print(arraySign(nums = [-1,-2,-3,-4,3,2,1]))
print(arraySign(nums = [1,5,0,2,-3]))
print(arraySign(nums = [-1,1,-1,1,-1]))
