"""
https://leetcode.com/problems/prime-subtraction-operation/description/
2601. Prime Subtraction Operation
You are given a 0-indexed integer array nums of length n.
You can perform the following operation as many times as you want:
Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
A strictly increasing array is an array whose each element is strictly greater than its preceding element.
Example 1:
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
Example 2:
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
Example 3:
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
Hint 1
Think about if we have many primes to subtract from nums[i]. Which prime is more optimal?
Hint 2
The most optimal prime to subtract from nums[i] is the one that makes nums[i] the smallest as possible and greater than nums[i-1].
"""
# Time - O(n*m*sqrt(m) or n*m+m*sqrt(m) or n+m*sqrt(m))
# Space - O(1)

from math import sqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True
            
        # prev = 0
        # for n in nums:
        #     upper_bound = n - prev # non inclusive
        #     largest_p = 0
        #     for i in reversed(range(2, upper_bound)):
        #         if is_prime(i):
        #             largest_p = i
        #             break
        #     if n - largest_p <= prev:
        #         return False
        #     prev = n - largest_p
        # return True
    
        # primes = [False, False] # primes[i] == True if i == prime
        # for i in range(2, max(nums)):
        #     if is_prime(i):
        #         primes.append(True)
        #     else:
        #         primes.append(False)
        # prev = 0
        # for n in nums:
        #     upper_bound = n - prev # non inclusive
        #     largest_p = 0
        #     for i in reversed(range(2, upper_bound)):
        #         if primes[i]:
        #             largest_p = i
        #             break
        #     if n - largest_p <= prev:
        #         return False
        #     prev = n - largest_p
        # return True
        
        primes = [0, 0] # primes[i] == True if i == prime
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])
        prev = 0
        for n in nums:
            upper_bound = n - prev # non inclusive
            largest_p = primes[upper_bound - 1]
            if n - largest_p <= prev:
                return False
            prev = n - largest_p
        return True

sol = Solution()
print(sol.primeSubOperation(nums = [4,9,6,10]))
print(sol.primeSubOperation(nums = [6,8,11,12]))
print(sol.primeSubOperation(nums = [5,8,3]))
