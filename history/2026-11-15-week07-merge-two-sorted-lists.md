# 2026-11-15 · 第 7 周 合并两个有序链表

- 在力扣中文版完成第 21 题，提交通过。 [提交记录](https://leetcode.cn/problems/merge-two-sorted-lists/submissions/760126274/)
- 区分了 Python 列表和 `ListNode`，练习了 `.val`、`.next` 和条件表达式。
- 先修正参数名与循环变量不一致的问题，再修正每轮同时推进两条链表导致跳过节点的问题。
- 用哑节点和尾指针拼接原节点，循环结束后接上剩余链表。时间 O(m + n)，额外空间 O(1)。

提交后复盘了两处等价简写：`while list1 and list2:` 判断两条链表还有节点，`cur.next = list1 if list1 else list2` 接上剩余链表。即使节点的 `.val` 为 0，节点本身的布尔值仍为真。

下一周是最大子数组和。
