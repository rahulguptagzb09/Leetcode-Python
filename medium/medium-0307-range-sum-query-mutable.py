"""
https://leetcode.com/problems/range-sum-query-mutable/description/
307. Range Sum Query - Mutable
Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""

# Time - O(m*logn)
# Space - O(n)

from typing import List


class BIT:

    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, v):
        while i < len(self.sums):
            self.sums[i] += v
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i
        return res


class NumArray:

    def __init__(self, nums: List[int]):
        self.b = BIT(len(nums))
        self.nums = nums
        for i, v in enumerate(nums):
            self.b.update(i + 1, v)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.b.update(index + 1, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.b.query(right + 1) - self.b.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
print(numArray.update(1, 2))
print(numArray.sumRange(0, 2))
