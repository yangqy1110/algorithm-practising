# 121. 买卖股票的最佳时机

- 来源：LeetCode
- 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
- 题型：贪心

## 描述

给一个数组 `prices`，其中 `prices[i]` 是第 `i` 天的股票价格。

你只能选择某一天买入，并在之后的某一天卖出。求能获得的最大利润；如果不能获利，返回 `0`。

## 例子

```text
输入：prices = [7, 1, 5, 3, 6, 4]
输出：5
解释：第 2 天以 1 买入，第 5 天以 6 卖出。
```

```text
输入：prices = [7, 6, 4, 3, 1]
输出：0
解释：价格一直下降，不进行交易。
```
