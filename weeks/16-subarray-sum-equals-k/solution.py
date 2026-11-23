"""560. 和为 K 的子数组"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pre_dic, prefix_sum, ans = {0: 1}, 0, 0
        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in pre_dic:
                ans = ans + pre_dic[prefix_sum - k]
            pre_dic[prefix_sum] = pre_dic.get(prefix_sum, 0) + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([1, -1, 1], 1) == 3
    assert solution.subarraySum([0, 0], 0) == 3
    assert solution.subarraySum([3], 3) == 1
    assert solution.subarraySum([-1], 0) == 0
    print("ok")
