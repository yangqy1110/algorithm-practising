# 2026-09-27 · 第 3 周 反转链表

## 这次做了什么

- 做完 [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)，迭代三指针。
- 先补了 Python 链表语法：`ListNode` 只有 `val` / `next`，空是 `None`。
- 自己写出的第一版用 `while cur and cur.next`，最后一格在循环外补；收成 `while cur`，返回 `pre`。
- 递归这周先不讲，以后再补。

下一周预告：二分查找。

## 自己的解法

```python
pre = None
cur = head
while cur:
    nex = cur.next
    cur.next = pre
    pre = cur
    cur = nex
return pre
```

## 已经讲清楚，下周不用从零再讲

1. 改 `cur.next` 之前必须先存后继，否则后半截丢了。
2. `while cur` 让每个节点（含最后一个）走同一套；循环结束 `cur` 是 `None`，新头是 `pre`。
3. `while cur and cur.next` 再 `if cur` 也对，只是把最后一格拆出去了。
4. 空链表、单节点不用特判。
5. 迭代空间 O(1)；递归能写，但调用栈是 O(n)，这周没展开。

## 和前两周的关系

哈希记「见过 / 还缺什么」，栈记「还没关上的左括号」。这周是改指针方向，不查表、不配对。
