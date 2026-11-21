"""LeetCode 226. 反转二叉树
https://leetcode.cn/problems/invert-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left, node.right = recur(node.right), recur(node.left)
            return node

        return recur(root)


if __name__ == "__main__":
    s = Solution()
    assert s.invertTree(None) is None
    leaf = TreeNode(1)
    assert s.invertTree(leaf) is leaf
    assert leaf.left is None and leaf.right is None
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(7, TreeNode(6), TreeNode(9))
    root = TreeNode(4, left, right)
    assert s.invertTree(root) is root
    assert root.left is right and root.right is left
    assert [right.left.val, right.right.val, left.left.val, left.right.val] == [9, 6, 3, 1]
    chain = TreeNode(1, TreeNode(2, TreeNode(3)))
    s.invertTree(chain)
    assert chain.left is None and chain.right.right.val == 3
    print("ok")
