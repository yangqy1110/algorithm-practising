"""
题目：53. 最大子数组和
链接：https://leetcode.cn/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-3, -1, -2]) == -1
    assert s.maxSubArray([0]) == 0
    print("ok")
