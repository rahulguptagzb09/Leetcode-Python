"""
https://leetcode.com/problems/new-21-game/description/
837. New 21 Game
Alice plays the following game, loosely based on the card game "21".
Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
Alice stops drawing numbers when she gets k or more points.
Return the probability that Alice has n or fewer points.
Answers within 10-5 of the actual answer are considered accepted.
Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
Constraints:
0 <= k <= n <= 104
1 <= maxPts <= 104
"""
# Time - O(k*m or k+m)
# Space - O(k+m)

def new21Game(n: int, k: int, maxPts: int) -> float:

    # cache  = {}
    # # Starting at score, return probability
    # def dfs(score):
    #     if score >= k:
    #         return 1 if score <= n else 0
    #     if score in cache:
    #         return cache[score]
    #     prob = 0
    #     for i in range(1, maxPts + 1):
    #         prob += dfs(score + i)
    #     cache[score] = prob / maxPts
    #     return cache[score]
    # return dfs(0)

    if k == 0:
        return 1.0
    windowSum = 0
    for i in range(k, k + maxPts):
        windowSum += 1 if i <= n else 0
    dp = {} # start at score -> probability
    for i in range(k - 1, -1, -1):
        dp[i] = windowSum / maxPts
        remove = 0
        if i + maxPts <= n:
            remove = dp.get(i + maxPts, 1)
        windowSum += dp[i] - remove
    return dp[0]

print(new21Game(n = 10, k = 1, maxPts = 10))
print(new21Game(n = 6, k = 1, maxPts = 10))
print(new21Game(n = 21, k = 17, maxPts = 10))
