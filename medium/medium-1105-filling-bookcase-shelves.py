"""
https://leetcode.com/problems/filling-bookcase-shelves/description/
1105. Filling Bookcase Shelves
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
Example 1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
Constraints:
1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
Hint 1
Use dynamic programming: dp(i) will be the answer to the problem for books[i:].
"""
# Time - O(n*w)
# Space - O(n)

from typing import List


def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
    # cache = {}
    # def helper(i):
    #     if i == len(books):
    #         return 0
    #     if i in cache:
    #         return cache[i]
    #     cur_width = shelfWidth
    #     max_height = 0
    #     cache[i] = float("inf")
    #     for j in range(i, len(books)):
    #         width, height = books[j]
    #         if cur_width < width:
    #             break
    #         cur_width -= width
    #         max_height = max(max_height, height)
    #         cache[i] = min(cache[i], helper(j + 1) + max_height)
    #     return cache[i]
    # return helper(0)

    dp = [0] * (len(books) + 1)
    for i in range(len(books) - 1, -1, -1):
        cur_width = shelfWidth
        max_height = 0
        dp[i] = float("inf")
        for j in range(i, len(books)):
            width, height = books[j]
            if cur_width < width:
                break
            cur_width -= width
            max_height = max(max_height, height)
            dp[i] = min(dp[i], dp[j + 1] + max_height)
    return dp[0]

print(minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4))
print(minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6))
