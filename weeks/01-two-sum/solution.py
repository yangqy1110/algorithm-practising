"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 字典存「还需要的那个数 → 当前下标」
        # 一次遍历 nums
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [i, dic[num]]
            else:
                dic[target - num] = i


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(s.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(s.twoSum([3, 3], 6)) == [0, 1]
    print("ok")
