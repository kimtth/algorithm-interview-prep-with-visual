# 86. Maximum Subarray

## Problem Description
Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

## Layman's Explanation
Find the slice of consecutive numbers that adds up to the biggest total.

**Example:** `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

Possible subarrays:
- `[4]` → sum = 4
- `[4, -1]` → sum = 3
- `[4, -1, 2]` → sum = 5
- `[4, -1, 2, 1]` → sum = 6 ✓ Maximum!

**Result:** `6`

## Algorithm: Kadane's Algorithm (Dynamic Programming)

### Key Insight
At each position, we decide: **start fresh** or **extend previous subarray**?

```
current_sum = max(num, current_sum + num)
```

If the current element alone is greater than adding it to the previous sum, **start a new subarray** here.

### Walkthrough

| Index | num | current_sum + num | Fresh start (num) | current_sum | best_sum |
|-------|-----|-------------------|-------------------|-------------|----------|
| 0 | -2 | - | -2 | -2 | -2 |
| 1 | 1 | -2+1=-1 | **1** | 1 | 1 |
| 2 | -3 | 1+(-3)=-2 | **-3** | -2 | 1 |
| 3 | 4 | -2+4=2 | **4** | 4 | 4 |
| 4 | -1 | **4+(-1)=3** | -1 | 3 | 4 |
| 5 | 2 | **3+2=5** | 2 | 5 | 5 |
| 6 | 1 | **5+1=6** | 1 | 6 | **6** |
| 7 | -5 | **6+(-5)=1** | -5 | 1 | 6 |
| 8 | 4 | **1+4=5** | 4 | 5 | 6 |

**Maximum subarray:** `[4, -1, 2, 1]` with sum `6`

## Approach 1: In-place Modification
```python
def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)
```

**Idea:** Modify array so each element holds "best sum ending here"

## Approach 2: Kadane's Algorithm (Clean)
```python
def maxSubArray(self, nums: List[int]) -> int:
    best_sum = -sys.maxsize
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    
    return best_sum
```

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass
- **Space Complexity:** O(1) - Only tracking two variables

## Key Insights
1. **Local vs Global optimal:** Track both current (local) and best (global) sums
2. **When to reset:** If previous sum is negative, it hurts us → start fresh
3. **DP formulation:** `dp[i] = max(nums[i], dp[i-1] + nums[i])`
4. **Space optimization:** Don't need full dp array, just previous value
5. **Edge case:** All negatives → return the largest (least negative) number
