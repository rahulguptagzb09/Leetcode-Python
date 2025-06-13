"""
https://leetcode.com/problems/course-schedule/description/
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
Hint 1
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Hint 2
Topological Sort via DFS - A great tutorial explaining the basic concepts of Topological Sort.
Hint 3
Topological sort could also be done via BFS.
"""
# Time - O(n+p)
# Space - O(n+p)

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prem_map = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prem_map[crs].append(pre)
        # visit set = all courses along the curr DFS path
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if prem_map[crs] == []:
                return True
            visit.add(crs)
            for pre in prem_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            prem_map[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

sol = Solution()
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
