"""
https://leetcode.com/problems/path-crossing/description/
1496. Path Crossing
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
Constraints:
1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""
# Time - O(n)
# Space - O(n)

def isPathCrossing(path: str) -> bool:
    dir = {
        "N": [0, 1], 
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0]
    }
    x, y = 0, 0
    visit = set() # (x, y)
    for c in path:
        visit.add((x, y))
        dx, dy = dir[c]
        x, y = x + dx, y + dy
        if (x, y) in visit:
            return True
    return False


print(isPathCrossing(path = "NES"))
print(isPathCrossing(path = "NESWW"))
