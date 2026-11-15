"""
LeetCode 21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = head = ListNode(0)

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 is None:
            cur.next = list2
        else:
            cur.next = list1

        return head.next


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
    assert to_list(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [
        1, 1, 2, 3, 4, 4
    ]
    assert s.mergeTwoLists(None, None) is None
    node = ListNode(0)
    assert s.mergeTwoLists(None, node) is node
    assert s.mergeTwoLists(node, None) is node
    assert to_list(s.mergeTwoLists(build_list([1, 2]), build_list([3, 4, 5]))) == [
        1, 2, 3, 4, 5
    ]
    print("ok")
