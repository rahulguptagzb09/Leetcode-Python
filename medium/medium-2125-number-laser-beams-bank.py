"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
2125. Number of Laser Beams in a Bank
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.
There is one laser beam between any two security devices if both conditions are met:
The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.
Return the total number of laser beams in the bank.
Example 1:
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
Example 2:
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
Constraints:
m == bank.length
n == bank[i].length
1 <= m, n <= 500
bank[i][j] is either '0' or '1'.
Hint 1
What is the commonality between security devices on the same row?
Hint 2
Each device on the same row has the same number of beams pointing towards the devices on the next row with devices.
Hint 3
If you were given an integer array where each element is the number of security devices on each row, can you solve it?
Hint 4
Convert the input to such an array, skip any row with no security device, then find the sum of the product between adjacent elements.
"""
# Time - O(n)
# Space - O(1)


from typing import List


def numberOfBeams(bank: List[str]) -> int:
    prev = bank[0].count("1")
    res = 0
    for i in range(1, len(bank)):
        curr = bank[i].count("1")
        if curr:
            res += (prev * curr)
            prev = curr
    return res

print(numberOfBeams(bank = ["011001","000000","010100","001000"]))
print(numberOfBeams(bank = ["000","111","000"]))
