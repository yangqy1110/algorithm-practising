"""
题目：15. 三数之和
链接：https://leetcode.cn/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    assert sorted(sorted(triple) for triple in s.threeSum([-1, 0, 1, 2, -1, -4])) == [
        [-1, -1, 2], [-1, 0, 1]
    ]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    print("ok")
