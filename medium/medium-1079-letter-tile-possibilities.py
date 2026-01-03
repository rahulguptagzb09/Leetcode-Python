"""
https://leetcode.com/problems/letter-tile-possibilities/
1079. Letter Tile Possibilities
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:
Input: tiles = "AAABBC"
Output: 188
Example 3:
Input: tiles = "V"
Output: 1
Constraints:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
Hint 1
Try to build the string with a backtracking DFS by considering what you can put in every position.
"""
# Time - O(2^n)
# Space - O(n)

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles) # char -> available count

        def backtrack():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1
            return res

        return backtrack()

sol = Solution()
print(sol.numTilePossibilities(tiles = "AAB"))
print(sol.numTilePossibilities(tiles = "AAABBC"))
print(sol.numTilePossibilities(tiles = "V"))
