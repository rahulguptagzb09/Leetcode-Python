"""
https://leetcode.com/problems/stone-game-ii/description/
1140. Stone Game II
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104
Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 104
Hint 1
Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.
"""
# Time - O(n^3)
# Space - O(n^2)

from typing import List


def stoneGameII(piles: List[int]) -> int:

    dp = {}
    # Num of stones alice gets
    def dfs(alice, i, M):
        if i == len(piles):
            return 0
        if (alice, i, M) in dp:
            return dp[(alice, i, M)]
        
        res = 0 if alice else float("inf")
        total = 0
        for X in range(1, 2 * M + 1):
            if i + X > len(piles):
                break
            total += piles[i + X - 1]
            if alice:
                res = max(res, total + dfs(not alice, i + X, max(M, X)))
            else:
                res = min(res, dfs(not alice, i + X, max(M, X)))   
        dp[(alice, i, M)] = res 
        return res
    
    return dfs(True, 0, 1)

print(stoneGameII(piles = [2,7,9,4,4]))
print(stoneGameII(piles = [1,2,3,4,5,100]))
