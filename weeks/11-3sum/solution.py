"""
题目：15. 三数之和
链接：https://leetcode.cn/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert sorted(sorted(triple) for triple in s.threeSum([-1, 0, 1, 2, -1, -4])) == [
        [-1, -1, 2], [-1, 0, 1]
    ]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    print("ok")
