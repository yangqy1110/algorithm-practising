"""
LeetCode 20. Valid Parentheses
https://leetcode.cn/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 只有 '(', '{', '[' 会进入栈
        # 遇到右括号：看栈顶是否匹配；栈空或不匹配则 false
        # 扫完后栈必须空
        dic = {")": "(", "]": "[", "}": "{"}
        lis = []
        for i in s:
            if i not in dic:
                lis.append(i)
            else:
                if len(lis) > 0 and dic[i] == lis[-1]:
                    lis.pop()
                else:
                    return False

        return len(lis) == 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    assert sol.isValid("") is True
    assert sol.isValid("(") is False
    assert sol.isValid(")") is False
    print("ok")
