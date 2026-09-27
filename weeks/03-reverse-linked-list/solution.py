"""
LeetCode 206. 反转链表
https://leetcode.cn/problems/reverse-linked-list/
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre


def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    vals: List[int] = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(build_list([1, 2]))) == [2, 1]
    assert to_list(s.reverseList(build_list([]))) == []
    print("ok")
