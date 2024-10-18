"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
1523. Count Odd Numbers in an Interval Range
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
Constraints:
0 <= low <= high <= 10^9
"""
# Time - O(1)


def countOdds(low: int, high: int) -> int:
    length = high - low + 1
    count = length // 2
    if length % 2 and low % 2:
        count += 1
    return count
    
print(countOdds(low = 3, high = 7))
print(countOdds(low = 8, high = 10))
