"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
1233. Remove Sub-Folders from the Filesystem
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
Constraints:
1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
Hint 1
Sort the folders lexicographically.
Hint 2
Insert the current element in an array and then loop until we get rid of all of their subfolders, repeat this until no element is left.
"""
# Time - O(n * l^2 or n*l)
# Space - O(n)

from typing import List

class Trie:
    def __init__(self) -> None:
        self.children = {} # string -> Trie
        self.end_of_folder = False
        
    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True

    def prefix_search(self, path):
        cur = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # folder_set = set(folder)
        # res = []
        # for f in folder:
        #     res.append(f)
        #     for i in range(len(f)):
        #         # /ab/ce
        #         if f[i] == "/" and f[:i] in folder_set:
        #             res.pop()
        #             break
        # return res

        trie = Trie()
        for f in folder:
            trie.add(f)
        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res

sol = Solution()
print(sol.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(sol.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
print(sol.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))
