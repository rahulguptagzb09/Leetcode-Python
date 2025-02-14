"""
https://leetcode.com/problems/sequential-digits/description/
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
Constraints:
10 <= low <= high <= 10^9
Hint 1
Generate all numbers with sequential digits and check if they are in the given range.
Hint 2
Fix the starting digit then do a recursion that tries to append all valid digits.
"""
# Time - O(1)
# Space - O(1)

from typing import List
from collections import deque


def sequentialDigits(low: int, high: int) -> List[int]:
    res = []
    queue = deque(range(1, 10))
    while queue:
        n = queue.popleft()
        if n > high:
            continue
        elif low <= n <= high:
            res.append(n)
        ones = n % 10
        if ones < 9:
            queue.append(n * 10 + (ones + 1))
    return res

print(sequentialDigits(low = 100, high = 300))
print(sequentialDigits(low = 1000, high = 13000))
