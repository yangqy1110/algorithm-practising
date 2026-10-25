# 2026-10-25 · 第 5 周 买卖股票的最佳时机

## 这次做了什么

- 做完 [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)。
- 自己写出一次遍历：维护历史最低价和最大利润。
- 去掉了不需要的 `enumerate` 和首元素特判，并把最大利润初值改成 `0`。
- 注意到 Python 的 `prices[1:]` 会复制列表；最终遍历整个数组，保持 O(1) 额外空间。

下一周预告：爬楼梯（动态规划入门）。

## 自己的解法

```python
min_num, res = prices[0], 0
for num in prices:
    res = max(res, num - min_num)
    min_num = min(min_num, num)
return res
```

## 已经讲清楚，下周不用从零再讲

1. 遍历到今天时，把今天当卖出日，最佳买入价就是此前最低价。
2. `min_num` 维护历史最低价，`res` 维护历史最大利润。
3. `res = 0` 表示允许不交易，下降数组自然返回 0。
4. 不使用下标时不需要 `enumerate`。
5. `prices[1:]` 简洁但会复制列表；遍历整个数组不影响结果，且额外空间 O(1)。
6. 不能直接用全局最大值减最小值，因为卖出日必须晚于买入日。
