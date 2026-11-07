"""
LeetCode 70. 爬楼梯
https://leetcode.cn/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur = 0, 1
        for _ in range(n):
            pre, cur = cur, pre + cur
        return cur


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8
    print("ok")
