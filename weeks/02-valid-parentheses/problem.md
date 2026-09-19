# 20. 有效的括号

- 来源：LeetCode
- 链接：https://leetcode.cn/problems/valid-parentheses/
- 题型：栈

## 描述

给一个只含 `()`、`[]`、`{}` 的字符串，判断是否合法：

- 左括号必须用**同类型**的右括号关掉
- 关掉的顺序必须正确（后开的先关）
- 每个右括号都要有对应的左括号

## 例子

```text
输入：s = "()"
输出：true
```

```text
输入：s = "()[]{}"
输出：true
```

```text
输入：s = "(]"
输出：false
```

```text
输入：s = "([)]"
输出：false
```

```text
输入：s = "{[]}"
输出：true
```
