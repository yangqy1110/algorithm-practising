"""
题目：200. 岛屿数量
链接：https://leetcode.cn/problems/number-of-islands/
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands([["0"]]) == 0
    assert s.numIslands([["1"]]) == 1
    assert s.numIslands([["1", "1"], ["1", "1"]]) == 1
    assert s.numIslands([["1", "0"], ["0", "1"]]) == 2
    assert s.numIslands([["1", "1", "0"], ["0", "0", "1"]]) == 2
    print("ok")
