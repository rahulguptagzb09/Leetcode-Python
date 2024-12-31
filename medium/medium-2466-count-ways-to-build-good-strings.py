"""
https://leetcode.com/problems/count-ways-to-build-good-strings/description/
2466. Count Ways To Build Good Strings
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.
A good string is a string constructed by the above process having a length between low and high (inclusive).
Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
Example 1:
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
Example 2:
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
Constraints:
1 <= low <= high <= 105
1 <= zero, one <= low
Hint 1
Calculate the number of good strings with length less or equal to some constant x.
Hint 2
Apply dynamic programming using the group size of consecutive zeros and ones.
"""
# Time - O(n)
# Space - O(n)

def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    # Backtracking Memoization
    # mod = 10**9 + 7
    # dp = {}
    # def dfs(length):
    #     if length > high:
    #         return 0
    #     if length in dp:
    #         return dp[length]
    #     dp[length] = 1 if length >= low else 0
    #     dp[length] += dfs(length + zero) + dfs(length + one)
    #     return dp[length] % mod
    # return dfs(0)

    # Dynamic Programming Tabular
    dp = { 0: 1 } # length -> number of strs
    mod = 10**9 + 7
    for i in range(1, high + 1):
        dp[i] = (dp.get(i - one, 0) + dp.get(i - zero, 0)) % mod
    return sum([dp[i] for i in range(low, high + 1)]) % mod

print(countGoodStrings(low = 3, high = 3, zero = 1, one = 1))
print(countGoodStrings(low = 2, high = 3, zero = 1, one = 2))
