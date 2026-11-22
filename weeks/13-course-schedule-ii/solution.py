"""
题目：210. 课程表 II
链接：https://leetcode.cn/problems/course-schedule-ii/
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    order = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert sorted(order) == list(range(4))
    positions = {course: i for i, course in enumerate(order)}
    assert all(positions[b] < positions[a] for a, b in [[1, 0], [2, 0], [3, 1], [3, 2]])
    print("ok")
