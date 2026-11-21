"""
题目：200. 岛屿数量
链接：https://leetcode.cn/problems/number-of-islands/
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return None
            if grid[i][j] == "0":
                return None
            grid[i][j] = "0"
            recur(i + 1, j)
            recur(i - 1, j)
            recur(i, j + 1)
            recur(i, j - 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    recur(i, j)
                    ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands([["0"]]) == 0
    assert s.numIslands([["1"]]) == 1
    assert s.numIslands([["1", "1"], ["1", "1"]]) == 1
    assert s.numIslands([["1", "0"], ["0", "1"]]) == 2
    assert s.numIslands([["1", "1", "0"], ["0", "0", "1"]]) == 2
    print("ok")
