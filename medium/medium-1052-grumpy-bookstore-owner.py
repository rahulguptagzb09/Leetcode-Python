"""
https://leetcode.com/problems/grumpy-bookstore-owner/
1052. Grumpy Bookstore Owner
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
Constraints:
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
Hint 1
Say the store owner uses their power in minute 1 to X and we have some answer A. If they instead use their power from minute 2 to X+1, we only have to use data from minutes 1, 2, X and X+1 to update our answer A.
"""
# Time - O(n)
# Space - O(1)

from typing import List


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    l = 0
    window, max_window = 0, 0
    satisfied = 0
    for r in range(len(customers)):
        if grumpy[r]:
            window += customers[r]
        else:
            satisfied += customers[r]
        
        if r - l + 1 > minutes:
            if grumpy[l]:
                window -= customers[l]
            l += 1
        max_window = max(window, max_window)
    return satisfied + max_window

print(maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
print(maxSatisfied(customers = [1], grumpy = [0], minutes = 1))
