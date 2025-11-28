# 78. Best Time to Buy and Sell Stock II

## Problem Description
Given an array `prices` where `prices[i]` is the price of a stock on day i, find the maximum profit. You can buy and sell multiple times (but must sell before buying again).

## Layman's Explanation
Unlike the single transaction version, here you can make as many trades as you want. The key insight is: **if the price goes up tomorrow, you should have bought today!**

**Example:** `prices = [7, 1, 5, 3, 6, 4]`

```
Day:    0   1   2   3   4   5
Price:  7   1   5   3   6   4
        ↓   ↑   ↓   ↑   ↓
            +4      +3
```

- Buy at 1, sell at 5 → profit +4
- Buy at 3, sell at 6 → profit +3
- Total: **7**

**Greedy Strategy:** Capture every upward movement!

```
if prices[i+1] > prices[i]:
    profit += prices[i+1] - prices[i]
```

## Algorithm Walkthrough
Given: `prices = [7, 1, 5, 3, 6, 4]`

| Day | Price | Next Price | Profit? | Running Total |
|-----|-------|------------|---------|---------------|
| 0   | 7     | 1          | No (↓)  | 0             |
| 1   | 1     | 5          | +4 (↑)  | 4             |
| 2   | 5     | 3          | No (↓)  | 4             |
| 3   | 3     | 6          | +3 (↑)  | 7             |
| 4   | 6     | 4          | No (↓)  | 7             |

**Result:** 7

## Why Greedy Works
Consider price sequence: `1 → 5 → 6`

**Option A:** Buy at 1, sell at 6 → profit = 5
**Option B:** Buy at 1, sell at 5; Buy at 5, sell at 6 → profit = 4 + 1 = 5

Both give the same result! Greedy captures all the upward movements which equals any optimal strategy.

## Code Explanation
```python
def maxProfit(self, prices: List[int]) -> int:
    result = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result
```

**One-liner alternative:**
```python
return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
```

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass through prices
- **Space Complexity:** O(1) - Only tracking total profit

## Key Insights
1. **Local Optimum = Global Optimum:** Every upward movement contributes to maximum profit
2. **No need to track buy/sell points:** Just add all positive differences
3. **Equivalent to peaks and valleys:** Buy at every valley, sell at every peak
4. **Compare with Stock I:** Here we take ALL profits, not just one transaction
