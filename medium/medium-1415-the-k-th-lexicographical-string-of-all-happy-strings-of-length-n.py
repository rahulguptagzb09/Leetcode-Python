"""
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
1415. The k-th Lexicographical String of All Happy Strings of Length n
A happy string is a string that:
consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
Constraints:
1 <= n <= 10
x1 <= k <= 100
Hint 1
Generate recursively all the happy strings of length n.
Hint 2
Sort them in lexicographical order and return the kth string if it exists.
"""
# Time - O(n)
# Space - O(n)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2**(n-1))
        res = []
        choices = "abc"
        left, right = 1, total_happy
        for _ in range(n):
            cur = left
            partition_size = (right - left + 1) // len(choices)
            # Polling 1 - 4, 5 - 8, 9 - 12
            for c in choices:
                # cur <= k < cur + partition_size
                if k in range(cur, cur + partition_size):
                    res.append(c)
                    left = cur
                    right = cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size

        return "".join(res)

sol = Solution()
print(sol.getHappyString(n = 1, k = 3))
print(sol.getHappyString(n = 1, k = 4))
print(sol.getHappyString(n = 3, k = 9))
