"""
LeetCode 704. 二分查找
https://leetcode.cn/problems/binary-search/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            n = (i + j) // 2
            if nums[n] < target:
                i = n + 1
            elif nums[n] > target:
                j = n - 1
            else:
                return n
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert s.search([5], 5) == 0
    assert s.search([5], -5) == -1
    print("ok")
