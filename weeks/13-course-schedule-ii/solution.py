"""
题目：210. 课程表 II
链接：https://leetcode.cn/problems/course-schedule-ii/
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        ok_nums = []
        while ready:
            now_course = ready.pop()
            ok_nums.append(now_course)
            for course in next_courses[now_course]:
                remaining[course] -= 1
                if remaining[course] == 0:
                    ready.append(course)

        return ok_nums if len(ok_nums) == numCourses else []


if __name__ == "__main__":
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    order = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert sorted(order) == list(range(4))
    positions = {course: i for i, course in enumerate(order)}
    assert all(positions[b] < positions[a] for a, b in [[1, 0], [2, 0], [3, 1], [3, 2]])
    print("ok")
