# 1. Two Sum

- 来源：LeetCode
- 链接：https://leetcode.com/problems/two-sum/
- 题型：哈希表

## 描述

给一个整数数组 `nums` 和一个目标值 `target`，找出两个不同下标 `i`、`j`，使得 `nums[i] + nums[j] == target`。假设恰好有一组答案。

## 例子

```text
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：2 + 7 = 9
```

```text
输入：nums = [3, 2, 4], target = 6
输出：[1, 2]
```

## 提示

先自己想暴力做法（两层循环），再想能不能用一次遍历 + 哈希表把「需要的另一个数」记下来。
