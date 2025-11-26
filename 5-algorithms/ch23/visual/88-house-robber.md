# 88. House Robber

## Problem Description
You are a robber planning to rob houses along a street. Each house has money, but **adjacent houses have connected security systems**. If two adjacent houses are robbed the same night, an alarm triggers.

Given an array of money amounts in each house, return the maximum money you can rob without triggering alarms.

## Layman's Explanation
You can't rob two houses in a row. Pick the best combination of non-adjacent houses.

**Example:** `nums = [1, 2, 3, 1]`

Options:
- Rob house 0 and house 2: 1 + 3 = **4** ✓
- Rob house 1 and house 3: 2 + 1 = 3
- Rob only house 0: 1
- Rob only house 2: 3

**Result:** `4`

**Example:** `nums = [2, 7, 9, 3, 1]`

Options:
- Rob houses 0, 2, 4: 2 + 9 + 1 = **12** ✓
- Rob houses 1, 3: 7 + 3 = 10
- Other combinations...

**Result:** `12`

## Algorithm: Dynamic Programming

### Key Insight
At each house, you have two choices:
1. **Skip it:** Take the best from previous house
2. **Rob it:** Take money + best from two houses back (can't rob adjacent)

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

### Walkthrough: `[2, 7, 9, 3, 1]`

| House | Money | Skip (dp[i-1]) | Rob (dp[i-2] + money) | Best (dp[i]) |
|-------|-------|----------------|----------------------|--------------|
| 0 | 2 | 0 | 0 + 2 = 2 | **2** |
| 1 | 7 | 2 | 0 + 7 = 7 | **7** |
| 2 | 9 | 7 | 2 + 9 = 11 | **11** |
| 3 | 3 | 11 | 7 + 3 = 10 | **11** |
| 4 | 1 | 11 | 11 + 1 = 12 | **12** |

**Maximum:** `12` (rob houses 0, 2, and 4)

## Approach 1: Recursion (Slow)
```python
def rob(self, nums: List[int]) -> int:
    def _rob(i: int) -> int:
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])
    
    return _rob(len(nums) - 1)
```

**Problem:** O(2^n) - overlapping subproblems without memoization

## Approach 2: Tabulation (Fast)
```python
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp.popitem()[1]
```

## Approach 3: Space Optimized
```python
def rob(self, nums: List[int]) -> int:
    prev2, prev1 = 0, 0
    
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current
    
    return prev1
```

**O(n) time, O(1) space!**

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) with optimization, O(n) with full dp array

## Key Insights
1. **Binary choice:** At each step, rob or skip
2. **Non-adjacent constraint:** Can only use dp[i-2] if we rob current
3. **Space optimization:** Only need last two values
4. **Similar problems:** House Robber II (circular), Delete and Earn
5. **Pattern:** "Take or skip" with constraints
