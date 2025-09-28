"""
https://leetcode.com/problems/jump-game-vii/
1871. Jump Game VII
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
Example 1:
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
Constraints:
2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
Hint 1
Consider for each reachable index i the interval [i + a, i + b].
Hint 2
Use partial sums to mark the intervals as reachable.
"""
# Time - O(n)
# Space - O(n)

from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, farthest = deque([0]), 0
        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        return False

sol = Solution()
print(sol.canReach(s = "011010", minJump = 2, maxJump = 3))
print(sol.canReach(s = "01101110", minJump = 2, maxJump = 3))
