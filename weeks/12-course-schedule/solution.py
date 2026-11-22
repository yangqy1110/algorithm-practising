"""LeetCode 207. 课程表
https://leetcode.cn/problems/course-schedule/
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        remaining = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            remaining[course] += 1

        next_courses = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            next_courses[prerequisite].append(course)

        ready = []
        for i, remain_num in enumerate(remaining):
            if remain_num == 0:
                ready.append(i)

        ok_num = 0
        while ready:
            now_course = ready.pop()
            ok_num += 1
            for course in next_courses[now_course]:
                remaining[course] -= 1
                if remaining[course] == 0:
                    ready.append(course)

        return ok_num == numCourses


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False
    assert s.canFinish(3, [[1, 0], [2, 0], [2, 1]]) is True
    assert s.canFinish(2, [[0, 1]]) is True
    assert s.canFinish(3, []) is True
    assert s.canFinish(1, [[0, 0]]) is False
    assert s.canFinish(4, [[1, 0], [2, 3], [3, 2]]) is False
    print("ok")
